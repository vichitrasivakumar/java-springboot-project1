package com.example.demo.repository;
import org.springframework.data.jpa.repository.JpaRepository;

import com.example.demo.entity.Passport;

public interface PassportRepository extends JpaRepository<Passport, Integer>
{


}
