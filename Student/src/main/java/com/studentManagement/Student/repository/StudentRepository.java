package com.studentManagement.Student.repository;
import org.springframework.data.jpa.repository.JpaRepository;
import com.studentManagement.Student.domain.Student;
public interface StudentRepository extends JpaRepository<Student, Long>,IStudentRepository {

}
