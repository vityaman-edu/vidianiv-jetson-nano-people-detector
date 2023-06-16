package ru.vidianiv.jetsonbackend.service;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Service;
import ru.vidianiv.jetsonbackend.objects.FeaturePacket;
import ru.vidianiv.jetsonbackend.objects.RecordEntity;
import ru.vidianiv.jetsonbackend.repository.RecordRepository;

import java.time.LocalDateTime;
import java.time.ZoneId;
import java.time.ZonedDateTime;
import java.util.Date;

@Service
public class RecordsService {

    private final RecordRepository recordRepository;
    private final Logger logger;

    private final Object lock;
    private LocalDateTime timestampBegin;
    private LocalDateTime timestampEnd;
    private long sumHumans;
    private int sumPackets;

    @Autowired
    public RecordsService(RecordRepository recordRepository) {
        this.recordRepository = recordRepository;
        lock = new Object();
        logger = LoggerFactory.getLogger(getClass());
    }

    public void processFeaturePackets(FeaturePacket[] packets) {
        if (packets.length == 0) return;

        synchronized (lock) {
            LocalDateTime timestamp = convertToLocalDateTime(packets[0].getTimestamp());
            if (timestampBegin == null) timestampBegin = timestamp;
            timestampEnd = timestamp;
            sumHumans += packets.length;
            sumPackets++;
        }
    }

    private static LocalDateTime convertToLocalDateTime(long timestamp) {
        ZonedDateTime zonedDateTime = new Date(timestamp).toInstant().atZone(ZoneId.systemDefault());
        return LocalDateTime.from(zonedDateTime);
    }

    @Scheduled(fixedRate = 60_000)
    public void flushEntity() {
        if (timestampBegin == null) return;

        synchronized (lock) {
            int averageHumans = (int) sumHumans / sumPackets;
            RecordEntity newRecord = new RecordEntity(
                    null,
                    timestampBegin,
                    timestampEnd,
                    averageHumans
            );
            RecordEntity savedRecord = recordRepository.save(newRecord);

            logger.info(String.format("Flushed record: %s", savedRecord));

            timestampBegin = null;
            timestampEnd = null;
            sumHumans = 0;
            sumPackets = 0;
        }
    }

}
