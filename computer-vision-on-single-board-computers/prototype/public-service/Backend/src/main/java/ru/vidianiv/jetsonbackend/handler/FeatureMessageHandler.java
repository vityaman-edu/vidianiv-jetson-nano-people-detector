package ru.vidianiv.jetsonbackend.handler;

import com.fasterxml.jackson.core.type.TypeReference;
import com.fasterxml.jackson.databind.ObjectMapper;
import lombok.SneakyThrows;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.integration.handler.AbstractMessageHandler;
import org.springframework.messaging.Message;
import org.springframework.stereotype.Component;
import ru.vidianiv.jetsonbackend.controller.StreamReceiver;
import ru.vidianiv.jetsonbackend.objects.FeaturePacket;
import ru.vidianiv.jetsonbackend.service.FeaturePacketProcessorService;
import ru.vidianiv.jetsonbackend.service.RecordsService;

@Component
public class FeatureMessageHandler extends AbstractMessageHandler {

    private final ObjectMapper objectMapper;
    private final StreamReceiver streamReceiver;
    private final RecordsService recordsService;
    private final FeaturePacketProcessorService featurePacketProcessorService;

    @Autowired
    public FeatureMessageHandler(ObjectMapper objectMapper, FeaturePacketProcessorService featurePacketProcessorService, StreamReceiver streamReceiver, RecordsService recordsService) {
        this.objectMapper = objectMapper;
        this.featurePacketProcessorService = featurePacketProcessorService;
        this.streamReceiver = streamReceiver;
        this.recordsService = recordsService;
    }

    @SneakyThrows
    @Override
    protected void handleMessageInternal(Message<?> message) {
        FeaturePacket[] packets = objectMapper.readValue((byte[]) message.getPayload(), new TypeReference<>(){});

        streamReceiver.processFeaturePackets(packets);
        recordsService.processFeaturePackets(packets);
        featurePacketProcessorService.processFeaturePackets(packets);
    }
}
