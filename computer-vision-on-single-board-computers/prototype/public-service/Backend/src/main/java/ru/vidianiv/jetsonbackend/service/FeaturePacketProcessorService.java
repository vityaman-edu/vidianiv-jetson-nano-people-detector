package ru.vidianiv.jetsonbackend.service;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import ru.vidianiv.jetsonbackend.util.feature.FeaturePacket;

@Service
public class FeaturePacketProcessorService {

    private final Logger logger;
    private final BroadcastMessageSendingService broadcastMessageSendingService;

    @Autowired
    public FeaturePacketProcessorService(BroadcastMessageSendingService broadcastMessageSendingService) {
        this.broadcastMessageSendingService = broadcastMessageSendingService;
        logger = LoggerFactory.getLogger(getClass());
    }

    public void processFeaturePacket(FeaturePacket packet) {
        logger.info(String.format("Received packet: %s", packet));
        broadcastMessageSendingService.convertAndSend("/stream/feature", packet);
    }

}
