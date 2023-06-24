package ru.vidianiv.jetsonbackend;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.scheduling.annotation.EnableScheduling;

@SpringBootApplication
@EnableScheduling
public class JetsonBackendApplication {

	public static void main(String[] args) {
		SpringApplication.run(JetsonBackendApplication.class, args);
	}

}
