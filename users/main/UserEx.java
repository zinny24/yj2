package main;

import java.sql.SQLException;

import service.UserSrv;

public class UserEx {

	public static void main(String[] args) throws SQLException {
		UserSrv service = new UserSrv();
		service.menu();
	}

}
