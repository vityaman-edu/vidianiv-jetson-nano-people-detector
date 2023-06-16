package ru.vidianiv.jetsonbackend.objects;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@AllArgsConstructor
@NoArgsConstructor
public class FeaturePacket {
    long timestamp;
    String label;
    double conf;
    Box box;

    @Data
    @AllArgsConstructor
    @NoArgsConstructor
    public static class Box {
        double left;
        double right;
        double top;
        double bottom;
    }
}