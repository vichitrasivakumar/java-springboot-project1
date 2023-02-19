package com.studentManagement.Student.dto;
import com.studentManagement.Student.domain.Student;
public class StudentDTO {
	private Long phoneNumber;
	private String name;
	private Integer age;
	private Character gender;
	private String course;
	private Integer planId;
	
	
	public StudentDTO(Long phoneNumber, String name, Integer age, Character gender, String course, Integer planId) {
		super();
		this.phoneNumber = phoneNumber;
		this.name = name;
		this.age = age;
		this.gender = gender;
		this.course = course;
		this.planId = planId;
	}
	public Long getPhoneNumber() {
		return phoneNumber;
	}
	public void setPhoneNumber(Long phoneNumber) {
		this.phoneNumber = phoneNumber;
	}
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public Integer getAge() {
		return age;
	}
	public void setAge(Integer age) {
		this.age = age;
	}
	public Character getGender() {
		return gender;
	}
	public void setGender(Character gender) {
		this.gender = gender;
	}
	public String getCourse() {
		return course;
	}
	public void setAddress(String course) {
		this.course = course;
	}
	public Integer getPlanId() {
		return planId;
	}
	public void setPlanId(Integer planId) {
		this.planId = planId;
	}
	@Override
	public String toString() {
		return "Customer [phoneNumber=" + phoneNumber + ", name=" + name + ", age=" + age + ", gender=" + gender
				+ ", course=" + course + ", planId=" + planId + "]";
	}
	
	public static  Student prepareCustomerEntity(StudentDTO StudentDTO)
	{
		 Student   StudentEntity = new  Student ();
		 StudentEntity .setPhoneNumber(StudentDTO.getPhoneNumber());
		 StudentEntity .setName(StudentDTO.getName());
		 StudentEntity .setGender(StudentDTO.getGender());
		 StudentEntity .setAge(StudentDTO.getAge());
		 StudentEntity .setCourse(StudentDTO.getCourse());
		 StudentEntity .setPlanId(StudentDTO.getPlanId());
		return  StudentEntity ;
		
	}
}


