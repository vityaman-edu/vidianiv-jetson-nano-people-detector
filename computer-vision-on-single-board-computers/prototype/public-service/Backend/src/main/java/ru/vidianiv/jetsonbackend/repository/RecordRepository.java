package ru.vidianiv.jetsonbackend.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import ru.vidianiv.jetsonbackend.objects.RecordEntity;

public interface RecordRepository extends JpaRepository<RecordEntity, Long> {
}
