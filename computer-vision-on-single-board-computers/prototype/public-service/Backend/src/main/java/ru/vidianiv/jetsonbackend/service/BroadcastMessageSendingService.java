package ru.vidianiv.jetsonbackend.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.messaging.simp.SimpMessagingTemplate;
import org.springframework.stereotype.Service;

@Service
public class BroadcastMessageSendingService {

    private final SimpMessagingTemplate template;

    @Autowired
    public BroadcastMessageSendingService(SimpMessagingTemplate template) {
        this.template = template;
    }

    public void convertAndSend(String destination, Object object) {
        template.convertAndSend(destination, object);
    }
}
