
---

# **📌 Database Schema Structure**
```plaintext
agile_performance_predictor
├── teams
│   ├── id (PK)
│   ├── name
│   ├── created_at
│
├── users
│   ├── id (PK)
│   ├── team_id (FK → teams.id)
│   ├── name
│   ├── email (UNIQUE)
│   ├── password (hashed)
│   ├── created_at
│
├── sprints
│   ├── id (PK)
│   ├── sprint_index (INTEGER)
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
│   ├── blockers (INTEGER)
│   ├── code_review_time (DECIMAL)
│   ├── bugs_found (INTEGER)
│   ├── sentiment_score (DECIMAL)
│   ├── sprint_duration (INTEGER)  
│   ├── test_automation (BOOLEAN)
│   ├── domain_complexity (INTEGER)
│   ├── non_functional_requirements_complexity (INTEGER)
│   ├── effort_variance (DECIMAL) -- % deviation from planned story points
│   ├── created_at
│
├── sprint_predictions
│   ├── id (PK)
│   ├── sprint_id (FK → sprints.id)
│   ├── predicted_sprint_velocity (DECIMAL)
│   ├── predicted_story_points (INTEGER)
│   ├── actual_completed_story_points (INTEGER, NULLABLE)
│   ├── created_at
|
├── training_data
│   ├── id (PK)
│   ├── team_size
│   ├── planned_story_points  
│   ├── completed_story_points
│   ├── blockers (INTEGER)
│   ├── code_review_time (DECIMAL)
│   ├── bugs_found (INTEGER)
│   ├── sentiment_score (DECIMAL)
│   ├── sprint_duration (INTEGER)  
│   ├── test_automation (BOOLEAN)
│   ├── domain_complexity (INTEGER)
│   ├── non_functional_requirements_complexity (INTEGER)
│   ├── sprint_start_date
│   ├── sprint_end_date
│   ├── created_at

```

---

### **📌 Table Descriptions**  

#### **1️⃣ `teams`**  
Stores team-related information.  
- **`id`** (PK) → Unique identifier for each team.  
- **`name`** → Name of the team.  
- **`created_at`** → Timestamp when the team was created.  

#### **2️⃣ `users`**  
Stores user details and their association with teams.  
- **`id`** (PK) → Unique user identifier.  
- **`name`** → User’s name.  
- **`email`** (UNIQUE) → User’s email for authentication.  
- **`password`** (hashed) → Securely stored user password.  
- **`created_at`** → Timestamp when the user account was created.  

#### **3️⃣ `sprints`**  
Contains sprint-related metadata.  
- **`id`** (PK) → Unique identifier for each sprint.  
- **`team_id`** (FK → `teams.id`) → The team executing this sprint.  
- **`sprint_index`** → Sprint number in sequence (e.g., Sprint 1, Sprint 2).  
- **`start_date`** → Start date of the sprint.  
- **`end_date`** → End date of the sprint.  
- **`planned_story_points`** → Story points estimated at the beginning of the sprint.  
- **`created_at`** → Timestamp when the sprint was created.  

#### **4️⃣ `sprint_metrics`**  
Stores performance metrics for each sprint.  
- **`id`** (PK) → Unique identifier.  
- **`sprint_id`** (FK → `sprints.id`) → Sprint being measured.  
- **`team_size`** → Number of people in the team during the sprint.  
- **`planned_story_points`** → Story points planned for the sprint.  
- **`blockers`** → Number of major blockers faced.  
- **`code_review_time`** (DECIMAL) → Avg. time taken for code reviews (in hours).  
- **`bugs_found`** → Number of bugs found during the sprint.  
- **`sentiment_score`** (INTEGER) → Team sentiment score based on feedback.  
- **`sprint_duration`** → Total sprint duration in days.  
- **`test_automation`** (BOOLEAN) → Whether test automation was used.  
- **`domain_complexity`** (INTEGER) → Rating (1-5) of domain complexity.  
- **`non_functional_requirements_complexity`** (INTEGER) → NFR complexity rating (1-5).  
- **`created_at`** → Timestamp when statistics were recorded.  

#### **5️⃣ `sprint_predictions`**  
Stores AI-predicted sprint performance.  
- **`id`** (PK) → Unique identifier.  
- **`sprint_id`** (FK → `sprints.id`) → Sprint for which prediction is made.  
- **`predicted_story_points`** (INTEGER) → Predicted story points completion.  
- **`actual_completed_story_points`** (INTEGER, NULLABLE) → Actual story points completed (updated after sprint).  
- **`created_at`** → Timestamp when prediction was generated.  

#### **4️⃣ `training_data`**  
Stores training data used to train the model.  
- **`id`** (PK) → Unique identifier.  
- **`team_size`** → Number of people in the team during the sprint.  
- **`planned_story_points`** → Story points planned for the sprint. 
- **`completed_story_points`** → Story points completed at the end of the sprint.  
- **`blockers`** → Number of major blockers faced.  
- **`code_review_time`** (DECIMAL) → Avg. time taken for code reviews (in hours).  
- **`bugs_found`** → Number of bugs found during the sprint.  
- **`sentiment_score`** (INTEGER) → Team sentiment score based on feedback.  
- **`sprint_duration`** → Total sprint duration in days.  
- **`test_automation`** (BOOLEAN) → Whether test automation was used.  
- **`domain_complexity`** (INTEGER) → Rating (1-5) of domain complexity.  
- **`non_functional_requirements_complexity`** (INTEGER) → NFR complexity rating (1-5).  
- **`sprint_start_date`** → Start date of the sprint.  
- **`sprint_end_date`** → End date of the sprint.  
- **`created_at`** → Timestamp when statistics were recorded.  

---


Each **team** can have multiple **sprints**, and each **sprint** has a corresponding **sprint metric record**.

---
