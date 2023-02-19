package com.studentManagement.Student;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import java.util.List;

import org.jboss.logging.Logger;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.context.ApplicationContext;
import com.studentManagement.Student.domain.Student;
import com.studentManagement.Student.dto.StudentDTO;
import com.studentManagement.Student.service.StudentService;

@SpringBootApplication
public class StudentApplication implements CommandLineRunner {
	public static Logger logger = Logger.getLogger(StudentApplication.class);
	
	@Autowired
	ApplicationContext context;
	@Autowired
	StudentService service;

	public static void main(String[] args) {
		SpringApplication.run(StudentApplication.class, args);
	}
	@Override
	public void run(String... args) throws Exception {
	StudentDTO Student1 = new StudentDTO(7022713754L, "Adam", 27, 'M', "java", 1);
	StudentDTO Student2 = new StudentDTO(7022713744L, "Susan", 25, 'F', "python", 2);
	StudentDTO Student3 = new StudentDTO(7022713745L, "Andrew", 27, 'M', "C", 2);
	// invoke service layer method to insert Customer
	service.insertStudent(Student1);
	service.insertStudent(Student2);
	service.insertStudent(Student3);
	
	 List<Student> cus1 = service.searchStudent(null, null, 'F', null);
	 logger.info(cus1);
	 
	  List<Student> cus2 = service.searchStudent("Adam", null, 'M', null);
	  logger.info(cus2);
	
	  List<Student> cus3 = service.searchStudent(null, null,null , 27);
	  logger.info(cus3);
	  
	 List<Student> cus4 = service.searchStudent("Susan","Alberta",null, null);
	 logger.info(cus4);
	

}
}
