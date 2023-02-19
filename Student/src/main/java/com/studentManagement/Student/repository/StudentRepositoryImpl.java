package com.studentManagement.Student.repository;
import java.util.List;
import javax.persistence.EntityManager;
import javax.persistence.EntityManagerFactory;
import javax.persistence.criteria.CriteriaBuilder;
import javax.persistence.criteria.CriteriaQuery;
import javax.persistence.criteria.Predicate;
import javax.persistence.criteria.Root;
import org.springframework.beans.factory.annotation.Autowired;
import com.studentManagement.Student.domain.Student;
public class StudentRepositoryImpl implements IStudentRepository  {
	private EntityManagerFactory emf;
	@Autowired
	public void setEntityManagerFactory(EntityManagerFactory emf) {
		this.emf = emf;
	}
	@Override
	public List<Student>searchStudent(String name, String address, Character gender, Integer age) {
		EntityManager em = emf.createEntityManager();
		CriteriaBuilder builder = em.getCriteriaBuilder();
		
		CriteriaQuery<Student> query = builder.createQuery(Student.class);
		Root<Student> root = query.from(Student.class);
		Predicate cName = builder.equal(root.get("name"), name);
		Predicate ccourse = builder.equal(root.get("course"), address);
		
		Predicate exp1 = builder.and(cName, ccourse);
		
		Predicate cGender = builder.equal(root.get("gender"), gender);
		Predicate cAge = builder.equal(root.get("age"), age);
		
		Predicate exp2 = builder.or(cGender,cAge);
				
		//Predicate dept = builder.equal(root.get("dept"), department);		
		query.where(builder.or(exp1, exp2));
		return em.createQuery(query.select(root)).getResultList();
}
}