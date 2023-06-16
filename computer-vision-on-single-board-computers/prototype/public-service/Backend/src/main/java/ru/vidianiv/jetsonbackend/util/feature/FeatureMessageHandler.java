package ru.vidianiv.jetsonbackend.util.feature;

import com.fasterxml.jackson.core.type.TypeReference;
import com.fasterxml.jackson.databind.ObjectMapper;
import lombok.SneakyThrows;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.integration.handler.AbstractMessageHandler;
import org.springframework.messaging.Message;
import org.springframework.stereotype.Component;
import ru.vidianiv.jetsonbackend.controller.StreamReceiver;
import ru.vidianiv.jetsonbackend.service.FeaturePacketProcessorService;

@Component
public class FeatureMessageHandler extends AbstractMessageHandler {

    private final ObjectMapper objectMapper;
    private final FeaturePacketProcessorService featurePacketProcessorService;
    private final StreamReceiver streamReceiver;

    @Autowired
    public FeatureMessageHandler(ObjectMapper objectMapper, FeaturePacketProcessorService featurePacketProcessorService, StreamReceiver streamReceiver) {
        this.objectMapper = objectMapper;
        this.featurePacketProcessorService = featurePacketProcessorService;
        this.streamReceiver = streamReceiver;
    }

    @SneakyThrows
    @Override
    protected void handleMessageInternal(Message<?> message) {
        FeaturePacket[] packets = objectMapper.readValue((byte[]) message.getPayload(), new TypeReference<>(){});
        streamReceiver.setLastFeatures(packets);
        for (FeaturePacket packet : packets) {
            featurePacketProcessorService.processFeaturePacket(packet);
        }
    }
}
