package com.studentManagement.Student.service;
import java.util.List;
import com.studentManagement.Student.dto.StudentDTO;
import com.studentManagement.Student.domain.Student;
public interface StudentService {
	public void insertStudent(StudentDTO  Student ) ;
	public List<Student> searchStudent(String name, String course, Character gender, Integer age) ;


}
