package com.example.demo;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.autoconfigure.cache.CacheAutoConfiguration;
import org.springframework.beans.factory.annotation.Autowired;

import com.example.demo.entity.Course;
import com.example.demo.entity.Student;
import com.example.demo.service.CourseService;
import com.example.demo.service.StudentService;
@SpringBootApplication(exclude = CacheAutoConfiguration.class)
public class MyProject1Application {
	@Autowired
	private StudentService studentService;
	
	@Autowired
	private CourseService courseService;
	
	public static void main(String[] args) {
		SpringApplication.run(MyProject1Application.class, args);
	}

	
	public void run(String... args) throws Exception 
	{
		Student student = new Student("Aditya");
		studentService.save(student);
		Course course = new Course("Spring Boot");
		courseService.save(course);
		student.addCourse(course);
		studentService.save(student);
		course.addStudent(student);
		courseService.save(course);
	}


}
