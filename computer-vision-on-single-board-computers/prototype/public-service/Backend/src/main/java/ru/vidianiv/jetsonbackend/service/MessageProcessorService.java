package ru.vidianiv.jetsonbackend.service;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import ru.vidianiv.jetsonbackend.dto.TextMessage;

@Service
public class MessageProcessorService {

    private final Logger logger;
    private final BroadcastMessageSendingService broadcastMessageSendingService;

    @Autowired
    public MessageProcessorService(BroadcastMessageSendingService broadcastMessageSendingService) {
        this.broadcastMessageSendingService = broadcastMessageSendingService;
        logger = LoggerFactory.getLogger(getClass());
    }

    public void processMessage(TextMessage textMessage) {
        logger.info(String.format("TextMessage: %s", textMessage));
        broadcastMessageSendingService.convertAndSend("/stream/video", textMessage);
    }

}
