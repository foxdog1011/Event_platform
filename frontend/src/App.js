import React, { useEffect, useState } from 'react';

function App() {
  const [events, setEvents] = useState([]);
  const [loading, setLoading] = useState(true); 
  const API_URL = process.env.REACT_APP_API_URL;

  useEffect(() => {
    fetch(`${API_URL}/api/events/`)
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(data => {
        setEvents(data);
        setLoading(false); 
      })
      .catch(error => {
        console.error('Fetch error:', error);
        setLoading(false); 
      });
  }, [API_URL]);

  return (
    <div>
      <h1>事件列表</h1>
      {loading ? ( 
        <p>加载中...</p>
      ) : (
        <ul>
          {events.map(event => (
            <li key={event.id}>
              <h2>{event.title}</h2>
              <p>{event.description}</p>
              <p>日期：{event.date}</p>
              <p>地点：{event.location}</p>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default App;
