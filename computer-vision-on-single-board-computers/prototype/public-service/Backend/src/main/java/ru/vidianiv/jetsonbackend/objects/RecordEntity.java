package ru.vidianiv.jetsonbackend.objects;

import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.time.LocalDateTime;

@Data
@AllArgsConstructor
@NoArgsConstructor

@Entity
public class RecordEntity {
    @Id
    @GeneratedValue
    Long id;

    @Temporal(TemporalType.TIMESTAMP)
    LocalDateTime timestampBegin;

    @Temporal(TemporalType.TIMESTAMP)
    LocalDateTime timestampEnd;

    Integer averageHumans;
}
