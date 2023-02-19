package com.studentManagement.Student.service;
import java.util.List;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.studentManagement.Student.domain.Student;
import com.studentManagement.Student.dto.StudentDTO;
import com.studentManagement.Student.repository.StudentRepository;
@Service("studentService")
public class StudentServiceImpl implements StudentService {
	 @Autowired
	  private StudentRepository  repository; 
	  
	public void insertStudent(StudentDTO Student) {
		repository.saveAndFlush(StudentDTO.prepareCustomerEntity(Student));
	}
	@Override
	public List<Student> searchStudent(String name, String course, Character gender, Integer age) {
		return repository.searchStudent(name, course, gender, age);
	}
	
	
}
