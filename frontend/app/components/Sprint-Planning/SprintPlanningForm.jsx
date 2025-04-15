// components/SprintPlanningForm.js
"use client";

import styles from "./page.module.css";
import { useState } from "react";
import Info from "../Info/Info";

export default function SprintPlanningForm({
  handleNext,
  handlePrevious,
  currentStep,
  steps,
  setSprintStartDate,
  setSprintEndDate
}) {

  const [activeForm, setActiveForm] = useState("create");
  const [sprintIndex, setSprintIndex] = useState("");
  const isComplete = sprintIndex.trim() !== "";
  const [sprintDuration, setSprintDuration] = useState("");
  const [sprintGoal, setSprintGoal] = useState("");
  const [startDate, setStartDate] = useState("");
  const [endDate, setEndDate] = useState("");


    const handleStartChange = (e) => {
      const value = e.target.value;
      setStartDate(value);
      setSprintStartDate(value); // send to parent
    };

    const handleEndChange = (e) => {
      const value = e.target.value;
      setEndDate(value);
      setSprintEndDate(value); // send to parent
    };



  return (
    <div className={styles.container}>
      <h2 className={styles.title}>Sprint Planning</h2>
      <div className={styles.toggle}>
        <button
          className={activeForm === "create" ? styles.active : ""}
          onClick={() => setActiveForm("create")}
        >
          Assigning Contraints
        </button>
        <button
          className={activeForm === "choose" ? styles.active : ""}
          onClick={() => setActiveForm("choose")}
        >
          Upload existing
        </button>
      </div>

      <Info />

      <div className={styles.scrollWrapper}>
        <div className={styles.formContainer}>
          {/* form index field*/}
          <div className={styles.headerRow}>
            <div className={styles.stepNumber}>1</div>
            <h2 className={styles.form_title}>Sprint Index</h2>
            <span className={isComplete ? styles.complete : styles.required}>
              {isComplete ? "Complete" : "Required"}
            </span>
          </div>

          <form className={styles.form_1}>
            <label className={styles.label}>Create an Index</label>
            <select
              className={styles.inputField}
              value={sprintIndex}
              onChange={(e) => setSprintIndex(e.target.value)}
            >
              <option value="">Example: Spring 5</option>
              <option value="Sprint 1">Sprint 1</option>
              <option value="Sprint 2">Sprint 2</option>
              <option value="Sprint 3">Sprint 3</option>
              <option value="Sprint 4">Sprint 4</option>
              <option value="Sprint 5">Sprint 5</option>
            </select>
          </form>

          <hr className={styles.separator} />

          {/* planned story points field */}
          <div className={styles.headerRow}>
            <div className={styles.stepNumber}>2</div>
            <h2 className={styles.form_title}>Planned Story Points</h2>
            <span
              className={sprintDuration ? styles.complete : styles.required}
            >
              {sprintDuration ? "Complete" : "Required"}
            </span>
          </div>

          <form className={styles.form_1}>
            <div className={styles.formField}>
              <label className={styles.label}>
                Estimated story points for the sprint{" "}
              </label>

              <input
                type="number"
                className={styles.inputField}
                value={sprintDuration}
                onChange={(e) => setSprintDuration(e.target.value)}
                placeholder="Example: 20"
                min={0}
              />

              <p className={styles.info}>
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  height="24px"
                  viewBox="0 -960 960 960"
                  width="10px"
                  fill="#000"
                >
                  <path d="M440-280h80v-240h-80v240Zm40-320q17 0 28.5-11.5T520-640q0-17-11.5-28.5T480-680q-17 0-28.5 11.5T440-640q0 17 11.5 28.5T480-600Zm0 520q-83 0-156-31.5T197-197q-54-54-85.5-127T80-480q0-83 31.5-156T197-763q54-54 127-85.5T480-880q83 0 156 31.5T763-763q54 54 85.5 127T880-480q0 83-31.5 156T763-197q-54 54-127 85.5T480-80Zm0-80q134 0 227-93t93-227q0-134-93-227t-227-93q-134 0-227 93t-93 227q0 134 93 227t227 93Zm0-320Z" />
                </svg>
                Please ensure you enter accurate details while filling out this
                form, as the data will be used to analyse sprint performance.
                You can review and modify your inputs later if needed. Take your
                time to provide the best estimates for each field to ensure
                meaningful insights.
              </p>
            </div>
          </form>

          <hr className={styles.separator} />

          <div className={styles.headerRow}>
            <div className={styles.stepNumber}>4</div>
            <h2 className={styles.form_title}>Sprint Dates</h2>
            <span
              className={
                startDate && endDate && startDate < endDate
                  ? styles.complete
                  : styles.required
              }
            >
              {startDate && endDate && startDate < endDate
                ? "Complete"
                : "Required"}
            </span>
          </div>

          <form className={styles.form_1}>
            <div className={styles.formFieldRow}>
              <div className={styles.formField}>
                <label className={styles.label}>Sprint Start Date</label>
                <input
                  type="date"
                  className={styles.inputDate}
                  value={startDate}
                  onChange={handleStartChange}
                />
              </div>

              <div className={styles.formField}>
                <label className={styles.label}>Sprint End Date</label>
                <input
                  type="date"
                  className={styles.inputDate}
                  value={endDate}
                  onChange={handleEndChange}
                  min={startDate}
                />
              </div>
            </div>
          </form>
        </div>
      </div>

      <div className={styles.buttonWrapper}>
        <button
          type="button"
          onClick={handlePrevious}
          className={styles.previousButton}
        >
          Previous
        </button>

        <button
          type="button"
          onClick={handleNext}
          disabled={currentStep === steps.length}
          className={styles.submitButton}
        >
          Next Step
        </button>
      </div>
    </div>
  );
}
