package com.report.report

import jakarta.annotation.PostConstruct
import org.springframework.stereotype.Component
import java.io.BufferedReader
import java.io.InputStreamReader


@Component
class MakeReport {
    @PostConstruct
    fun generateReport () {
        val pb = ProcessBuilder("python", "C:\\Users\\sclee\\spring-boot\\report\\src\\main\\python\\report.py")

        // 프로세스 시작
        var process = pb.start()

        val reader = BufferedReader(InputStreamReader(process.inputStream))

        var line: String?
        while (reader.readLine().also { line = it } != null) {
            println(line)
        }

        val exitCode = process.waitFor()

        if (exitCode == 0) {
            println("프로세스가 정상적으로 종료되었습니다.")
        } else {
            println("프로세스가 비정상적으로 종료되었습니다. 종료 코드: " + exitCode + "\n프로세스 종료 이유 : " + process.errorReader().readLine())
        }
    }
}