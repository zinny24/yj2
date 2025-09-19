import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [username, setUsername] = useState('');
  const [userList, setUserList] = useState([]);
  const [editingId, setEditingId] = useState(null);
  const [editingUsername, setEditingUsername] = useState('');
  const [message, setMessage] = useState('');

  const apiUrl = 'http://localhost:8080/api/users';

  useEffect(() => {
    handleRes();
  }, []);

  const handleReq = async () => {
    try {
      if (!username.trim()) return alert('이름을 입력하세요.');
      await axios.post(apiUrl, { username });
      setUsername('');
      setMessage('저장되었습니다.');
      clearMessageAfterDelay();
      handleRes();
    } catch (err) {
      console.error(err);
    }
  };

  const handleRes = async () => {
    try {
      const response = await axios.get(apiUrl);
      setUserList(response.data);
    } catch (err) {
      console.error(err);
    }
  };

  const handleDelete = async (id) => {
    try {
      await axios.delete(`${apiUrl}/${id}`);
      setMessage('삭제되었습니다.');
      clearMessageAfterDelay();
      handleRes();
    } catch (err) {
      console.error(err);
    }
  };

  const handleEdit = (id, currentName) => {
    setEditingId(id);
    setEditingUsername(currentName);
  };

  const handleUpdate = async (id) => {
    try {
      await axios.put(`${apiUrl}/${id}`, { username: editingUsername });
      setEditingId(null);
      setEditingUsername('');
      setMessage('수정되었습니다.');
      clearMessageAfterDelay();
      handleRes();
    } catch (err) {
      console.error(err);
    }
  };

  const clearMessageAfterDelay = () => {
    setTimeout(() => setMessage(''), 3000);
  };

  return (
    <div className="container">
      <h2>Username 저장 / 불러오기 / 수정 / 삭제</h2>

      {message && <div className="message">{message}</div>}

      <input
        type="text"
        className="input-field"
        placeholder="Enter username"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
      />
      <button className="button" onClick={handleReq}>Spring으로 데이터 전송</button>
      <button className="button" onClick={handleRes}>Database 가져오기</button>

      <h3>저장된 유저 목록:</h3>
      <ul className="user-list">
        {userList.map((user) => (
          <li key={user.id} className="user-item">
            {editingId === user.id ? (
              <>
                <input
                  className="input-field"
                  value={editingUsername}
                  onChange={(e) => setEditingUsername(e.target.value)}
                />
                <button className="button" onClick={() => handleUpdate(user.id)}>저장</button>
                <button className="button" onClick={() => setEditingId(null)}>취소</button>
              </>
            ) : (
              <>
                {user.username}{' '}
                <button className="button" onClick={() => handleEdit(user.id, user.username)}>수정</button>
                <button className="button" onClick={() => handleDelete(user.id)}>삭제</button>
              </>
            )}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
