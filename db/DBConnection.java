package db;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class DBConnection {

	private static final String DB_URL = "jdbc:mysql://localhost:3306/users";
	private static final String DB_ID = "root";
	private static final String DB_PWD = "1234";
	
	public static Connection getConnection() throws SQLException {
		return DriverManager.getConnection(DB_URL, DB_ID, DB_PWD);
	}
}







