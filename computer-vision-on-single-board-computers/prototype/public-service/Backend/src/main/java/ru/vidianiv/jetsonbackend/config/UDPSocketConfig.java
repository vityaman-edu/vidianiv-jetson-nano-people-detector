package ru.vidianiv.jetsonbackend.config;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.integration.dsl.IntegrationFlow;
import org.springframework.integration.ip.dsl.Udp;
import ru.vidianiv.jetsonbackend.handler.FeatureMessageHandler;

@Configuration
public class UDPSocketConfig {

    @Value("${udp-receiving-port}")
    private int receivingPort;

    @Value("${udp-receiving-buffer-size}")
    private int receivingBufferSize;

    private final FeatureMessageHandler featureMessageHandler;

    @Autowired
    public UDPSocketConfig(FeatureMessageHandler featureMessageHandler) {
        this.featureMessageHandler = featureMessageHandler;
    }

    @Bean
    public IntegrationFlow udpInbound() {
        return IntegrationFlow.from(Udp.inboundAdapter(receivingPort).receiveBufferSize(receivingBufferSize))
                .channel("udpReceivingChannel")
                .handle(featureMessageHandler)
                .get();
    }

}
