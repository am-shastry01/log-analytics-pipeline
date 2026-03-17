CREATE TABLE endpoint_stats (
	endpoint TEXT,
	total_requests INT,
	avg_response_time FLOAT
);

CREATE TABLE error_stats (
	endpoint TEXT,
	error_count INT
);