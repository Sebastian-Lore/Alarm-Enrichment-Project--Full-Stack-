CREATE TABLE sites (
    site_id SERIAL PRIMARY KEY,
    location TEXT NOT NULL,
    contact_info TEXT,
    priority INTEGER
);

CREATE TABLE alarms (
    alarm_id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    site_id INTEGER REFERENCES sites(site_id),
    alarm_code TEXT NOT NULL,
    severity TEXT CHECK (severity IN ('Critical', 'Major', 'Minor', 'Warning')),
    status TEXT DEFAULT 'New'
);

CREATE TABLE alarm_enrichment (
    enriched_id SERIAL PRIMARY KEY,
    alarm_id INTEGER REFERENCES alarms(alarm_id),
    site_info TEXT,
    additional_context TEXT,
    processed_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
