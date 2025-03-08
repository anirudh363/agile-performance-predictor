
---

# **📌 Database Schema Structure**
```plaintext
agile_performance_predictor
├── teams
│   ├── id (PK)
│   ├── name
│   ├── created_at
│
├── sprints
│   ├── id (PK)
│   ├── team_id (FK → teams.id)
│   ├── sprint_number
│   ├── start_date
│   ├── end_date
│   ├── planned_story_points
│   ├── created_at
│
├── sprint_metrics
│   ├── id (PK)
│   ├── sprint_id (FK → sprints.id)
│   ├── team_size
│   ├── planned_story_points
│   ├── completed_story_points
│   ├── blockers
│   ├── review_time
│   ├── bugs_found
│   ├── sentiment_score
│   ├── sprint_duration
│   ├── test_automation
│   ├── domain_complexity
│   ├── nfr_load
│   ├── created_at
│
├── predicted_results
│   ├── id (PK)
│   ├── team_id (FK → teams.id)
│   ├── predicted_sprint_velocity
│   ├── completed_story_points (optional, if user enters it)
│   ├── created_at
│
├── users
│   ├── id (PK)
│   ├── name
│   ├── email
│   ├── password
│   ├── created_at
```

---

# **📌 Table Descriptions**

### **1️⃣ `teams` Table**
| Column      | Type         | Description                      |
|------------|-------------|----------------------------------|
| id         | SERIAL (PK)  | Unique team identifier          |
| name       | VARCHAR(255) | Name of the team                |
| created_at | TIMESTAMP    | When the team was created       |

---

### **2️⃣ `sprints` Table**
| Column               | Type        | Description                           |
|----------------------|------------|---------------------------------------|
| id                  | SERIAL (PK) | Unique sprint identifier             |
| team_id             | INT (FK)    | References `teams.id`                 |
| sprint_number       | INT         | Sprint number for the team           |
| start_date         | DATE        | Sprint start date                     |
| end_date           | DATE        | Sprint end date                       |
| planned_story_points | INT        | Estimated story points for the sprint |
| created_at          | TIMESTAMP   | Timestamp of sprint creation         |

---

### **3️⃣ `sprint_metrics` Table**  
| Column               | Type        | Description                                  |
|----------------------|------------|----------------------------------------------|
| id                  | SERIAL (PK) | Unique metric ID                            |
| sprint_id           | INT (FK)    | References `sprints.id`                     |
| team_size          | INT         | Number of team members                      |
| planned_story_points | INT        | Expected story points for the sprint        |
| completed_story_points | INT      | Actual completed story points               |
| blockers           | INT         | Number of blockers/issues encountered       |
| review_time        | FLOAT       | Average code review time (in hours)         |
| bugs_found        | INT         | Number of bugs found                        |
| sentiment_score    | FLOAT       | Team morale (0-1 scale)                     |
| sprint_duration    | INT         | Duration of sprint (1-10 days)              |
| test_automation    | FLOAT       | % of test automation (0-1 scale)            |
| domain_complexity  | INT         | Complexity of the sprint domain (1-5 scale) |
| nfr_load          | INT         | Non-functional requirement load (1-5 scale) |
| created_at         | TIMESTAMP   | Timestamp of metric entry                   |

---

# **📌 ER Diagram**
Here’s how the tables are connected:

```plaintext
    teams
      ▲
      │ (1-to-Many)
      ▼
    sprints
      ▲
      │ (1-to-1)
      ▼
    sprint_metrics
```

Each **team** can have multiple **sprints**, and each **sprint** has a corresponding **sprint metric record**.

---
