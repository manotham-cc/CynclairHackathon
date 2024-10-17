create schema test;

use test;

CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    full_name VARCHAR(100),
    email VARCHAR(100),
    role VARCHAR(50) CHECK (role IN ('Detection Engineer', 'Admin', 'Analyst', 'Investigator')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert mock data
INSERT INTO users (username, full_name, email, role)
VALUES 
('alice01', 'Alice Johnson', 'alice.johnson@company.com', 'Detection Engineer'),
('bob99', 'Bob Richards', 'bob.richards@company.com', 'Admin'),
('charlie_m', 'Charlie Moore', 'charlie.moore@company.com', 'Analyst'),
('dana_i', 'Dana Ingram', 'dana.ingram@company.com', 'Investigator');

CREATE TABLE devices (
    device_id INT AUTO_INCREMENT PRIMARY KEY,
    hostname VARCHAR(100) NOT NULL,
    ip_address VARCHAR(15) NOT NULL,
    operating_system VARCHAR(50),
    user_id INT,
    last_seen TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- Insert mock data
INSERT INTO devices (hostname, ip_address, operating_system, user_id, last_seen)
VALUES
('server-001', '192.168.1.10', 'Linux', 1, NOW() - INTERVAL 2 DAY),
('laptop-020', '192.168.1.20', 'Windows 10', 2, NOW() - INTERVAL 5 HOUR),
('workstation-001', '192.168.1.30', 'macOS', 3, NOW() - INTERVAL 3 DAY),
('laptop-002', '192.168.1.40', 'Windows 11', 4, NOW() - INTERVAL 1 DAY);

CREATE TABLE alerts (
    alert_id INT AUTO_INCREMENT PRIMARY KEY,
    alert_type VARCHAR(100) NOT NULL,
    description TEXT,
    severity_level ENUM('Low', 'Medium', 'High', 'Critical'),
    device_id INT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (device_id) REFERENCES devices(device_id)
);

-- Insert mock data
INSERT INTO alerts (alert_type, description, severity_level, device_id)
VALUES
('Malware Detection', 'Potential malware found on server-001.', 'Critical', 1),
('Unauthorized Access', 'Multiple failed login attempts on workstation-001.', 'High', 3),
('Data Exfiltration', 'Unusual outbound traffic detected.', 'Medium', 2),
('Suspicious Activity', 'Suspicious process running on laptop-002.', 'Low', 4);

CREATE TABLE incidents (
    incident_id INT AUTO_INCREMENT PRIMARY KEY,
    incident_type VARCHAR(100),
    alert_id INT,
    investigator_id INT,
    status ENUM('Open', 'In Progress', 'Resolved', 'Closed'),
    resolution_details TEXT,
    investigation_start TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    investigation_end TIMESTAMP NULL,
    FOREIGN KEY (alert_id) REFERENCES alerts(alert_id),
    FOREIGN KEY (investigator_id) REFERENCES users(user_id)
);

-- Insert mock data
INSERT INTO incidents (incident_type, alert_id, investigator_id, status, resolution_details, investigation_end)
VALUES
('Malware Response', 1, 4, 'Resolved', 'Malware removed and system restored.', NOW()),
('Unauthorized Access Investigation', 2, 3, 'In Progress', 'Still investigating user credentials.', NULL),
('Data Exfiltration Review', 3, 2, 'Open', '', NULL);

CREATE TABLE threat_intelligence (
    ti_id INT AUTO_INCREMENT PRIMARY KEY,
    threat_name VARCHAR(100),
    description TEXT,
    severity ENUM('Low', 'Medium', 'High', 'Critical'),
    last_seen TIMESTAMP,
    source VARCHAR(100)
);

-- Insert mock data
INSERT INTO threat_intelligence (threat_name, description, severity, last_seen, source)
VALUES
('Cobalt Strike', 'Advanced persistent threat using C2 frameworks.', 'High', NOW() - INTERVAL 3 DAY, 'Threat Intel Service A'),
('Emotet', 'Banking trojan spread via phishing emails.', 'Critical', NOW() - INTERVAL 1 DAY, 'Threat Intel Service B'),
('Ransomware XYZ', 'A new strain of ransomware affecting Windows systems.', 'Critical', NOW() - INTERVAL 5 DAY, 'Threat Intel Service C'),
('APT-29', 'State-sponsored espionage group targeting government sectors.', 'Medium', NOW() - INTERVAL 7 DAY, 'Threat Intel Service D');