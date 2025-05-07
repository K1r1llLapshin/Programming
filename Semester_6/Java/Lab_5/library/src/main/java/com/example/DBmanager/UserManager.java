package com.example.DBmanager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class UserManager extends DatabaseManager {
    
    // Добавление нового пользователя
    public boolean addUser(String login, String password) throws SQLException {
        validateConnection();
        
        // Проверяем, существует ли уже пользователь с таким логином (ID)
        if (exists("users", "login", login)) {
            System.out.println("Пользователь с логином '" + login + "' уже существует");
            return false;
        }
        
        // Добавляем нового пользователя
        String sql = "INSERT INTO users (login, password) VALUES (?, ?)";
        try (PreparedStatement stmt = connection.prepareStatement(sql)) {
            stmt.setString(1, login);
            stmt.setString(2, password);
            
            int affectedRows = stmt.executeUpdate();
            if (affectedRows > 0) {
                System.out.println("Пользователь '" + login + "' успешно добавлен");
                return true;
            }
        }
        
        return false;
    }
    
    
    // Проверка логина и пароля
    public boolean validateUser(String login, String password) throws SQLException {
        validateConnection();
        
        String sql = "SELECT 1 FROM users WHERE login = ? AND password = ?";
        try (PreparedStatement stmt = connection.prepareStatement(sql)) {
            stmt.setString(1, login);
            stmt.setString(2, password);
            
            try (ResultSet rs = stmt.executeQuery()) {
                return rs.next();
            }
        }
    }
    
}