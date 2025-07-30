package service;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import java.util.Scanner;

import db.DBConnection;

public class UserSrv {

	//html
	Scanner sc = new Scanner(System.in);
	
	//종료를 누르기 전까지 무한 반복 실행 = Web Service
	//while(true) {}
	
	
	public void addUser() throws SQLException {
		System.out.println("");
		System.out.println("--- 회원가입을 진행합니다. ---");
		System.out.println("");
		
		System.out.print("이름 > ");
		String sc_name = sc.nextLine();
		
		System.out.print("이메일 > ");
		String sc_email = sc.nextLine();
		
		System.out.print("비밀번호 > ");
		String sc_passwd = sc.nextLine();
		
		String sql = "INSERT INTO users(name, email, passwd) VALUES(?, ?, ?);";
		
		Connection conn = DBConnection.getConnection();
		PreparedStatement pstmt = conn.prepareStatement(sql);
		pstmt.setString(1, sc_name);
		pstmt.setString(2, sc_email);
		pstmt.setString(3, sc_passwd);
		pstmt.executeUpdate();
		
		System.out.println("회원가입이 완료되었습니다.");
		
	}
	
	public void listUsers() {
		System.out.println("");
		System.out.println("--- 회원전체 목록을 출력합니다.");
		System.out.println("");
	}
	
	public void updateEmail() {
		System.out.println("");
		System.out.println("이메일을 수정할 회원 ID를 입력하세요.");
		System.out.println("");
	}
	
	public void deleteUsers() {
		System.out.println("");
		System.out.println("삭제할 회원 ID를 입력하세요.");
		System.out.println("");
	}
	
	//ui/ux 메소드로 만들기
	public void menu() throws SQLException {
		
		while(true) {			
			System.out.println("---- 회원 관리 시스템 -----");
			System.out.println("1. 회원등록");
			System.out.println("2. 전체 회원 목록");
			System.out.println("3. 이메일 수정");
			System.out.println("4. 회원 삭제");
			System.out.println("0. 프로그램 종료");
			System.out.print("선택 > ");
			
			
			int choice = sc.nextInt();
			sc.nextLine(); //버퍼(저장 메모리) 비우기
			
			switch(choice) {
			case 1:
				addUser();
				break;
				
			case 2:
				listUsers();
				break;
				
			case 3:
				updateEmail();
				break;
				
			case 4:
				deleteUsers();
				break;
				
			case 0:
				System.out.println("프로그램을 종료합니다.");
				return;
				
			default:
				System.out.println("메뉴를 다시 선택해 주세요.");
			}
			
		}
		
		
		
		
	}
}








