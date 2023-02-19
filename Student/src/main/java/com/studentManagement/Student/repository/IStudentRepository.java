package com.studentManagement.Student.repository;
import java.util.List;
import com.studentManagement.Student.domain.Student;
public interface IStudentRepository {
	public List<Student> searchStudent(String name, String course, Character gender, Integer age);
	}


