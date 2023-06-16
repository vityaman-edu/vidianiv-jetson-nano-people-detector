package ru.vidianiv.jetsonbackend.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.messaging.handler.annotation.MessageMapping;
import org.springframework.messaging.handler.annotation.Payload;
import org.springframework.stereotype.Controller;
import ru.vidianiv.jetsonbackend.dto.TextMessage;
import ru.vidianiv.jetsonbackend.service.MessageProcessorService;

@Controller
public class MessageReceiver {

    private final MessageProcessorService messageProcessorService;

    @Autowired
    public MessageReceiver(MessageProcessorService messageProcessorService) {
        this.messageProcessorService = messageProcessorService;
    }

    @MessageMapping("/broadcast")
    public void receiveMessage(@Payload TextMessage textMessage) {
        messageProcessorService.processMessage(textMessage);
    }

}
