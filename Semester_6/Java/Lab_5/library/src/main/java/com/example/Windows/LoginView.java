package com.example.Windows;

import java.io.IOException;
import java.sql.SQLException;

import com.example.DBmanager.UserManager;

import javafx.geometry.Insets;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.Alert;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.PasswordField;
import javafx.scene.control.TextField;
import javafx.scene.layout.ColumnConstraints;
import javafx.scene.layout.GridPane;
import javafx.scene.layout.HBox;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;

public class LoginView extends VBox {
    private final TextField loginField = new TextField();
    private final PasswordField passwordField = new PasswordField();
    UserManager db = new UserManager();
    
   LoginView(Stage primaryStage) {
        // Основные настройки layout
        setAlignment(Pos.CENTER); 
        setSpacing(20); 
        setPadding(new Insets(20));
        
        // Создание элементов интерфейса
        Label titleLabel = new Label("Авторизация");
        titleLabel.setStyle("-fx-font-size: 20px; -fx-font-weight: bold;");
        
        // Сетка для полей ввода
        GridPane inputGrid = new GridPane();
        inputGrid.setHgap(10);
        inputGrid.setVgap(10);
        inputGrid.setAlignment(Pos.CENTER);
        
        // Настройка колонок
        ColumnConstraints col1 = new ColumnConstraints(); 
        col1.setHalignment(javafx.geometry.HPos.RIGHT);
        col1.setMinWidth(100);
        
        ColumnConstraints col2 = new ColumnConstraints();
        col2.setHalignment(javafx.geometry.HPos.LEFT);
        col2.setMinWidth(200);
        
        inputGrid.getColumnConstraints().addAll(col1, col2);
        
        // Добавление полей ввода в сетку
        inputGrid.add(new Label("Логин:"), 0, 0);
        loginField.setPromptText("Введите логин");
        inputGrid.add(loginField, 1, 0);
        
        inputGrid.add(new Label("Пароль:"), 0, 1);
        passwordField.setPromptText("Введите пароль");
        inputGrid.add(passwordField, 1, 1);
        
        // Панель кнопок
        HBox buttonBox = new HBox(20);
        buttonBox.setAlignment(Pos.CENTER);
        
        Button loginButton = new Button("Вход");
        loginButton.setStyle("-fx-min-width: 100px; -fx-base: #0096c9;");
        loginButton.setOnAction(e -> handleLogin(primaryStage));
        
        Button registerButton = new Button("Регистрация");
        registerButton.setStyle("-fx-min-width: 100px;");
        registerButton.setOnAction(e -> handleRegister(primaryStage));
        
        buttonBox.getChildren().addAll(loginButton, registerButton);

         // Добавление всех элементов в основной layout
        getChildren().addAll(titleLabel, inputGrid, buttonBox);
    }
    
    private void showError(String message) {
        Alert alert = new Alert(Alert.AlertType.ERROR);
        alert.setTitle("Ошибка входа");
        alert.setHeaderText(null);
        alert.setContentText(message);
        alert.showAndWait();
    }
    
    private void showHomeScreen(Stage primaryStage, String login) throws IOException {
        HomeView homeView = new HomeView(primaryStage, login);
        Scene scene = new Scene(homeView, 1000, 500);
        primaryStage.setScene(scene);
    }
    
    private void showRegisterScreen(Stage primaryStage) throws IOException {
        RegisterView registerView = new RegisterView(primaryStage);
        Scene scene = new Scene(registerView, 1000, 500);
        primaryStage.setScene(scene);
    }
   
    private void handleLogin(Stage primaryStage) {
        String login = loginField.getText().trim();
        String password = passwordField.getText().trim();
        
        if (login.isEmpty() || password.isEmpty()) {
            showError("Логин и пароль не могут быть пустыми");
            return;
        }

        try {
            db.connect("library.db");
            
            if (db.validateUser(login, password))
                showHomeScreen(primaryStage, login);
            else 
                showError("Неверный логин или пароль");
        } 
        catch (SQLException e) {
            System.err.println("Ошибка базы данных: " + e.getMessage());
        } 
        catch (IOException e) {
            System.err.println("Ошибка загрузки интерфейса: " + e.getMessage());
        } 
        finally {
            db.close();
        }
    }
    
    private void handleRegister(Stage primaryStage) {
        try {
            showRegisterScreen(primaryStage);
        } 
        catch (IOException e) {
            System.err.println("Ошибка загрузки интерфейса регистрации: " + e.getMessage());
        }
    }
    
    
}