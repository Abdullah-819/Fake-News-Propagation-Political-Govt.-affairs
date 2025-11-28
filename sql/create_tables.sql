-- DataBase setup
-- users table
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    role VARCHAR(70) NOT NULL,
    influence_score FLOAT DEFAULT 1.0,
    trust_level FLOAT DEFAULT 1.0,
    alignment VARCHAR(60)
);

-- fake_news table
CREATE TABLE IF NOT EXISTS fake_news (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id),
    connected_user_id INT REFERENCES users(id),
    relationship_strength FLOAT DEFAULT 1.0
);

-- propagation_log table
CREATE TABLE IF NOT EXISTS propagation_log (
    id SERIAL PRIMARY KEY,
    news_id INT REFERENCES fake_news(id),
    user_id INT REFERENCES users(id),
    step_number INT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
