[ 파이썬 설치하기 ]
	※ 별도의 개발도구 설치는 xxx
https://www.python.org/downloads/
	PATH 추가하면서 설치
IDLE 실행시 Shell 화면
	>>>
1. 인터프리터 언어
2. 동적타이핑 언어
	타입(자료형)이 자유롭게 변형 가능
	숫자와 '문자열'을 구분하는것이 중요함!!!

[ 웹 흐름 ]
 == 요청 응답 처리 흐름
 == 클라이언트 서버 흐름
1. 클라이언트(사용자,브라우저)가 서비스를 이용하려고 요청
	↓ HTTP 요청
	↑ 웹 페이지(HTML 문서)를 반환
2. 서버는 요청에 대해 응답

[ 스프링에서는 어떻게 처리하는지 ? ]
1. 클라이언트가 요청
2. DS == FrontController
3. 요청에 맞는 Controller를 반환하는 HM
4. 사용자에게 응답하기위한 페이지를 반환하는 VR

[ NoSQL ]
1. 우리가 배운 SQL
	RDBMS에서 사용함
	관계형 DBMS
	MySQL, Oracle, ...
2. 현재 웹시장에서는 아직 RDBMS가 최적이라고 여겨짐
3. 비정형, 대용량 데이터를 다루는 분야
	빅데이터, AI
	파이썬
4. NoSQL은
	여러 DB 서버를 클러스터링하여
	하나의 DB로 사용하자!는 컨셉
5. 확장성이 좋고, 빠름(성능이 좋음)
6. "JOIN을 많이 안쓴다."
	애초에 관계가 없으니 JOIN 연산 불가능

[ NODE.js ]
1. (기본) JavaScript 학습하기
	https://www.inflearn.com/course/%EC%BD%94%EB%93%9C%ED%8C%A9%ED%86%A0%EB%A6%AC-%EC%9E%90%EB%B0%94%EC%8A%A4%ED%81%AC%EB%A6%BD%ED%8A%B8-%ED%92%80%EC%BD%94%EC%8A%A4
2. (프론트 사이드 프레임워크) NODE.js, React 등 학습하기
	https://www.inflearn.com/course/%EB%94%B0%EB%9D%BC%ED%95%98%EB%A9%B0-%EB%B0%B0%EC%9A%B0%EB%8A%94-%EB%85%B8%EB%93%9C-%EB%A6%AC%EC%95%A1%ED%8A%B8-%EC%98%81%ED%99%94%EC%82%AC%EC%9D%B4%ED%8A%B8-%EB%A7%8C%EB%93%A4%EA%B8%B0
3. 프론트 사이드에서 활용하는 프레임워크
4. 내장된 서버 라이브러리가 존재함
	→ 별도의 웹서버(아파치 톰캣)없이 서버 처리 가능
	→ DB 기능 제작 가능
	→ 서버 사이드 로직을 처리할 수 있음

[ REST API ]
1. HTTP 통신에 최적화된 설계 규칙을 지킨 API 입니다.
2. 클라이언트는 URI로 요청하길 원하는 자원을 선택
	+
	자원에 대한 처리를 서버에 요청
	ex) https://blog.naver.com/coding_helper/222876211482
			/coding_helper >> coding_helper 닉네임을 가진 사람의
			/222876211482 >> 222876211482 번째 게시글을
			( 생략 ) >> 보여주세요! == SELECTONE

[ HTTP method ]
블로그 확인

[ ORM(Object Relational Mapping, 객체 관계 매핑) ]
	자바 객체와 SQL 사이의 자동 매핑 기능을 지원
	JDBC 어떻게 매핑했지?
		VO vo=new VO();
		vo.setXxx(rs.getString("NAME"));
		vo.setXxx(rs.getInt("AGE"));
	JdbcTemplate(템플릿 패턴) 어떻게 매핑했지?
		class VORowMap<VO> 정의
	결론) ORM 등장전에는 자바 개발자가 (자동 매핑이 안되니까) 직접 코드를 작성하여 매핑
1. Mybatis
	대표적인 ORM 프레임워크
	SQL을 별도의 파일(.xml)로 분리하여 관리
	SQL이 프로그래밍 코드와 분리되었기때문에 SQL 변경이 발생해도 컴파일을 다시 안해도 ㄱㅊ
	자바 코드가 바뀐것이 아니기 때문임
2. JPA
	ORM 구현을 위한 JAVA API
	메서드 호출만으로 쿼리문을 수행할수있도록 해줌
	복잡한 쿼리문은 수행이 다소 어려움
	https://www.inflearn.com/course/jpa-spring-data-%EA%B8%B0%EC%B4%88
