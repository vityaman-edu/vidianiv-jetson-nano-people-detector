package ru.vidianiv.jetsonbackend.service;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import ru.vidianiv.jetsonbackend.objects.FeaturePacket;

@Service
public class FeaturePacketProcessorService {

    private final Logger logger;
    private final BroadcastMessageSendingService broadcastMessageSendingService;

    @Autowired
    public FeaturePacketProcessorService(BroadcastMessageSendingService broadcastMessageSendingService) {
        this.broadcastMessageSendingService = broadcastMessageSendingService;
        logger = LoggerFactory.getLogger(getClass());
    }

    public void processFeaturePackets(FeaturePacket[] packets) {
        for (FeaturePacket packet : packets) {
            logger.info(String.format("Received packet: %s", packet));
        }
        broadcastMessageSendingService.convertAndSend("/stream/feature", packets);
    }

}
