"use client";

import styles from "./page.module.css";
import { useState } from "react";

import Info from "../Info/Info";

export default function SprintMetricsForm({
  currentStep,
  steps,
  handlePrevious,
  sprintStartDate,
  sprintEndDate
}) {
  const [teamSize, setTeamSize] = useState("");
  const [plannedPoints, setPlannedPoints] = useState("");
  const [blockers, setBlockers] = useState("");
  const [codeReviewTime, setCodeReviewTime] = useState("");
  const [bugsReported, setBugsReported] = useState("");
  const [sentimentValue, setSentimentValue] = useState(1);
  const [testAutomation, setTestAutomation] = useState(true);
  const [domainComplexity, setDomainComplexity] = useState(1);
  const [nonFunctionalComplexity, setNonFunctionalComplexity] = useState();


  const [activeForm, setActiveForm] = useState("create");

  const handleChange = (e) => {
    setSentimentValue(parseFloat(e.target.value));
    console.log(sentimentValue);
    
  };

  const handleSubmit = () => {
    if (
      !teamSize ||
      !plannedPoints ||
      !blockers ||
      !codeReviewTime ||
      !bugsReported ||
      !sentimentValue ||
      !testAutomation ||
      !sprintStartDate ||
      !sprintEndDate ||
      sprintStartDate >= sprintEndDate
    ) {
      alert("Please complete all required fields.");
      return;
    }

    const formData = {
      teamSize,
      plannedPoints,
      blockers,
      codeReviewTime,
      bugsReported,
      sentimentValue,
      sprintStartDate,
      sprintEndDate,
      testAutomation,
    };

    console.log("Submitting data:", formData);
    // You can replace this with a POST request to your backend.
  };


  console.log("start : ",sprintStartDate ); 
  console.log("end : ",sprintEndDate ); 
  
  return (
    <div className={styles.container}>
      <h2 className={styles.title}>Sprint Metrics</h2>
      <div className={styles.toggle}>
        <button
          className={activeForm === "create" ? styles.active : ""}
          onClick={() => setActiveForm("create")}
        >
          Metrics Input
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
          {/* team size field */}
          <div className={styles.headerRow}>
            <div className={styles.stepNumber}>1</div>
            <h2 className={styles.form_title}>Team Size</h2>
            <span className={teamSize ? styles.complete : styles.required}>
              {teamSize ? "Complete" : "Required"}
            </span>
          </div>
          <form className={styles.form_1}>
            <div className={styles.formField}>
              <label className={styles.label}>
                How big is your dream team this sprint? Count everyone -- even
                the coffee powered ones!
              </label>
              <input
                type="number"
                className={styles.inputField}
                value={teamSize}
                onChange={(e) => setTeamSize(e.target.value)}
                placeholder="e.g. 5"
                min="1"
              />
            </div>
          </form>

          <hr className={styles.separator} />

          {/* planned sotry points field */}
          <div className={styles.headerRow}>
            <div className={styles.stepNumber}>2</div>
            <h2 className={styles.form_title}>Planned Story Points</h2>
            <span className={plannedPoints ? styles.complete : styles.required}>
              {plannedPoints ? "Complete" : "Required"}
            </span>
          </div>
          <form className={styles.form_1}>
            <div className={styles.formField}>
              <label className={styles.label}>Enter Planned Story Points</label>
              <input
                type="number"
                className={styles.inputField}
                value={plannedPoints}
                onChange={(e) => setPlannedPoints(e.target.value)}
                placeholder="e.g. 20"
                min="1"
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

          {/* blockers field */}
          <div className={styles.headerRow}>
            <div className={styles.stepNumber}>3</div>
            <h2 className={styles.form_title}>Blockers</h2>
            <span className={blockers ? styles.complete : styles.required}>
              {blockers ? "Complete" : "Required"}
            </span>
          </div>
          <form className={styles.form_1}>
            <div className={styles.formField}>
              <label className={styles.label}>Enter Number of Blockers</label>
              <input
                type="number"
                className={styles.inputField}
                value={blockers}
                onChange={(e) => setBlockers(e.target.value)}
                placeholder="e.g. 3"
                min="0"
              />
            </div>
          </form>

          <hr className={styles.separator} />

          {/* code review time field */}
          <div className={styles.headerRow}>
            <div className={styles.stepNumber}>4</div>
            <h2 className={styles.form_title}>Code Review Time</h2>
            <span
              className={codeReviewTime ? styles.complete : styles.required}
            >
              {codeReviewTime ? "Complete" : "Required"}
            </span>
          </div>
          <form className={styles.form_1}>
            <div className={styles.formField}>
              <label className={styles.label}>
                Enter Code Review Time (in hours)
              </label>
              <input
                type="number"
                step="0.1"
                className={styles.inputField}
                value={codeReviewTime}
                onChange={(e) => setCodeReviewTime(e.target.value)}
                placeholder="e.g. 2.5"
                min="0"
              />
            </div>
          </form>

          <hr className={styles.separator} />

          {/* bugs reported field */}
          <div className={styles.headerRow}>
            <div className={styles.stepNumber}>5</div>
            <h2 className={styles.form_title}>Bugs Reported</h2>
            <span className={bugsReported ? styles.complete : styles.required}>
              {bugsReported ? "Complete" : "Required"}
            </span>
          </div>
          <form className={styles.form_1}>
            <div className={styles.formField}>
              <label className={styles.label}>Enter Bugs Reported</label>
              <input
                type="number"
                className={styles.inputField}
                value={bugsReported}
                onChange={(e) => setBugsReported(e.target.value)}
                placeholder="e.g. 3"
                min="0"
              />
            </div>
          </form>

          <hr className={styles.separator} />

          {/* emoji slider for semtiment analysis */}
          <div className={styles.headerRow}>
            <div className={styles.stepNumber}>6</div>
            <h2 className={styles.form_title}>Sentiment Score</h2>
            <span
              className={sentimentValue ? styles.complete : styles.required}
            >
              {sentimentValue ? "Complete" : "Required"}
            </span>
          </div>

          <div className={styles.sentimentScoreContainer}>
            <p>
              How did the team feel this sprint? Vibes check — from 😁 to 😡,
              rate the mood!
            </p>
            <div className={styles.sliderWrapper}>
              <input
                type="range"
                min={0}
                max={1}
                step={0.01}
                value={sentimentValue}
                onChange={handleChange}
                className={styles.slider}
              />
              <div className={styles.emojiRow}>
                <span>😁</span>
                <span>😊</span>
                <span>😐</span>
                <span>😟</span>
                <span>😡</span>
              </div>
            </div>
          </div>

          <hr className={styles.separator} />

          <div className={styles.headerRow}>
            <div className={styles.stepNumber}>7</div>
            <h2 className={styles.form_title}>Sprint Dates</h2>
            <span
              className={
                sprintStartDate &&
                sprintEndDate &&
                sprintStartDate < sprintEndDate
                  ? styles.complete
                  : styles.required
              }
            >
              {sprintStartDate &&
              sprintEndDate &&
              sprintStartDate < sprintEndDate
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
                  value={sprintStartDate}
                  disabled
                />
              </div>

              <div className={styles.formField}>
                <label className={styles.label}>Sprint End Date</label>
                <input
                  type="date"
                  className={styles.inputDate}
                  value={sprintEndDate}
                  disabled
                />
              </div>
            </div>
          </form>

          <hr className={styles.separator} />

          <div className={styles.headerRow}>
            <div className={styles.stepNumber}>6</div>
            <h2 className={styles.form_title}>Test Automation</h2>
            <span
              className={testAutomation ? styles.complete : styles.required}
            >
              {testAutomation ? "Complete" : "Required"}
            </span>
          </div>

          <form className={styles.form_1}>
            <div className={styles.formField}>
              <label className={styles.label}>
                Was Test Automation Implemented?
              </label>
              <label className={styles.switch}>
                <input
                  type="checkbox"
                  checked={testAutomation}
                  onChange={(e) => setTestAutomation(e.target.checked)}
                />
                <span className={styles.switchSlider}></span>
              </label>
            </div>
          </form>

          <hr className={styles.separator} />

          <div className={styles.headerRow}>
            <div className={styles.stepNumber}>9</div>
            <h2 className={styles.form_title}>Domain Complexity</h2>
            <span
              className={domainComplexity ? styles.complete : styles.required}
            >
              {domainComplexity ? "Complete" : "Required"}
            </span>
          </div>

          <form className={styles.form_1}>
            <label className={styles.label}>
              How brain-bending was the work this sprint? Rate the domain
              complexity—from 'smooth sailing' to 'mind maze' 🧠🌀
            </label>

            <div className={styles.sliderWrapper}>
              <input
                type="range"
                min="1"
                max="5"
                step="1"
                value={domainComplexity}
                onChange={(e) => setDomainComplexity(Number(e.target.value))}
                className={styles.slider}
              />

              <div className={styles.emojiRow}>
                <span>🪶</span>
                <span>😊</span>
                <span>😐</span>
                <span>🙁</span>
                <span>🧠</span>
              </div>
            </div>
          </form>

          <hr className={styles.separator} />

          <div className={styles.headerRow}>
            <div className={styles.stepNumber}>10</div>
            <h2 className={styles.form_title}>Non-functional Complexity</h2>
            <span
              className={
                nonFunctionalComplexity ? styles.complete : styles.required
              }
            >
              {nonFunctionalComplexity ? "Complete" : "Required"}
            </span>
          </div>

          <form className={styles.form_1}>
            <div className={styles.formField}>
              <label className={styles.label}>
                Enter Non-functional Complexity
              </label>
              <input
                type="number"
                className={styles.inputField}
                value={nonFunctionalComplexity}
                onChange={(e) => setNonFunctionalComplexity(e.target.value)}
                placeholder="e.g. 2"
                min="1"
              />
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
          className={styles.submitButton}
          onClick={handleSubmit}
        >
          Continue Predicting!
        </button>
      </div>
    </div>
  );
}
