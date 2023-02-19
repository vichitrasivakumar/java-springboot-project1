package com.example.demo.service;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import com.example.demo.entity.Passport;
import com.example.demo.repository.PassportRepository;

@Service
public class PassPortService {
	@Autowired
	private PassportRepository passportRepository;
	
	@Transactional
	public Passport save(Passport passport) {
		return passportRepository.save(passport);
	}
}
