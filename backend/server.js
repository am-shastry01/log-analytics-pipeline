const express = require("express")
const { Pool } = require("pg")
const cors = require("cors")

const app = express()
app.use(cors())

const pool = new Pool({
    user: "postgres",
    host: "postgres",
    database: "sales_analytics_pipline",
    password: "Aryan930054",
    port: "5432",
})

app.get("/api/endpoints", async (req, res) => {

    const result = await pool.query(
        "SELECT * FROM endpoint_stats ORDER BY total_requests DESC"
    )

    res.json(result.rows)
})

app.get("/api/errors", async (req, res) => {

    const result = await pool.query(
        "SELECT * FROM error_stats ORDER BY error_count DESC"
    )

    res.json(result.rows)
})

app.listen(5000, () => {
    console.log("Server running on port 5000")
})