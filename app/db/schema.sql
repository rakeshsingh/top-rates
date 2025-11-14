CREATE TABLE IF NOT EXISTS Bank (
    bank_id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    bank_old_name TEXT,
    bank_rss_id TEXT,
    bank_uninum TEXT,
    bank_type TEXT NOT NULL,
    routing_number TEXT,
    bank_website TEXT,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    last_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);