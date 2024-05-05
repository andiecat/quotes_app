import { useEffect, useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
  let [quotes, setQuotes] = useState(null);

  useEffect(() => {
    fetch('http://localhost:8080/quotes')
      .then(res => res.json())
      .then(data => setQuotes(data))
  }, []);

  return (
    <>
      {
        quotes == null && <p>Loading...</p>
      }
    
      {
        quotes != null &&
        <>
          <h1>Quotes</h1>
          <ol>
            {
              quotes.map((quote) => 
                <li>
                  <div className="card">
                    {quote.text}
                    <br/>
                    { quote.name != null && quote.name }
                    { quote.author != null && <>
                      {quote.title} by {quote.author}
                    </> }
                  </div>
                </li>
              )
            }
          </ol>
        </>
      }
    </>
  )
}

export default App
