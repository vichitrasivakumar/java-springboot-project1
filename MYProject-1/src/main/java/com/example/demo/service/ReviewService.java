package com.example.demo.service;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import  com.example.demo.entity.Review;
import  com.example.demo.repository.ReviewRepository;

@Service
public class ReviewService {
	@Autowired
	private ReviewRepository reviewRepository;
	
	public Review findById(int id) {
		return reviewRepository.findById(id).get();
	}
	
	@Transactional
	public Review save(Review review) {
		return reviewRepository.save(review);
	}
	
	@Transactional
	public void remove(Review review) {
		reviewRepository.delete(review);
	}
}
