package ru.vidianiv.jetsonbackend.controller;

import jakarta.annotation.PostConstruct;
import lombok.Getter;
import lombok.Setter;
import lombok.SneakyThrows;
import org.opencv.core.*;
import org.opencv.highgui.HighGui;
import org.opencv.imgcodecs.Imgcodecs;
import org.opencv.imgproc.Imgproc;
import org.opencv.videoio.VideoCapture;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.scheduling.annotation.EnableScheduling;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Component;
import ru.vidianiv.jetsonbackend.service.BroadcastMessageSendingService;
import ru.vidianiv.jetsonbackend.objects.FeaturePacket;

import java.util.Arrays;

@Component
public class StreamReceiver {

    static {
        System.loadLibrary(Core.NATIVE_LIBRARY_NAME);
    }

    private final BroadcastMessageSendingService messageSendingService;
    private final Logger logger;

    @Value("${rtsp-ip}")
    private String rtspIp;

    @Value("${rtsp-port}")
    private int rtspPort;

    @Value("${rtsp-url}")
    private String rtspUrl;

    private VideoCapture capture;
    private Mat receivedImage;
    private MatOfByte encodedImage;

    @Autowired
    public StreamReceiver(BroadcastMessageSendingService messageSendingService) {
        this.messageSendingService = messageSendingService;
        this.logger = LoggerFactory.getLogger(getClass());
    }

    @PostConstruct
    public void init() {
        String url = String.format("rtsp://%s:%s/%s", rtspIp, rtspPort, rtspUrl);
        capture = new VideoCapture(url);
        receivedImage = new Mat();
        encodedImage = new MatOfByte();
    }

    @Getter @Setter
    public FeaturePacket[] lastFeatures;

    public void processFeaturePackets(FeaturePacket[] packets) {
        lastFeatures = packets;
    }

    @Scheduled(fixedDelay = 1)
    public void sendNewFrame() {
        if (!capture.read(receivedImage)) return;
        visualize();
        processImage();
    }

    private void visualize() {
        for (FeaturePacket feature : lastFeatures) {
            FeaturePacket.Box box = feature.getBox();
            Imgproc.rectangle(
                    receivedImage,
                    new Point(box.getLeft(), box.getTop()),
                    new Point(box.getRight(), box.getBottom()),
                    new Scalar(100, 255, 100),
                    2
            );
            String label = String.format("%s, %.2f", feature.getLabel(), feature.getConf());
            Imgproc.putText(
                    receivedImage,
                    label,
                    new Point(box.getLeft(), box.getTop()),
                    Imgproc.FONT_HERSHEY_PLAIN,
                    1,
                    new Scalar(10, 10, 10)
            );
        }

        HighGui.imshow("Camera", receivedImage);
        HighGui.waitKey(1);
    }

    @SneakyThrows
    private void processImage() {
        Imgcodecs.imencode(".jpg", receivedImage, encodedImage);
        byte[] encodedImageBytes = encodedImage.toArray();
        logger.info(String.format("RTSP packet size: %s", encodedImageBytes.length));
        short[] encodedImageUbytes = new short[encodedImageBytes.length];
        for (int i = 0; i < encodedImageBytes.length; i++) {
            encodedImageUbytes[i] = (short) (encodedImageBytes[i] >= 0 ? encodedImageBytes[i] : 256 + encodedImageBytes[i]);
        }
        messageSendingService.convertAndSend("/stream/video", Arrays.toString(encodedImageUbytes));
    }

}
