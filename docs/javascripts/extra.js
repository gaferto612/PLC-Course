/* ============================================================
   PLC-FastTrack — site-wide interactivity
   - Animated stat counters
   - Scroll-reveal sections
   - Mini "scan cycle" PLC demo on the landing page
   ============================================================ */

(function () {
  const ready = (fn) =>
    document.readyState !== "loading"
      ? fn()
      : document.addEventListener("DOMContentLoaded", fn);

  /* ---------- Animated counters ---------- */
  function animateCounter(el) {
    const target = parseFloat(el.dataset.count || "0");
    const suffix = el.dataset.suffix || "";
    const duration = 1200;
    const start = performance.now();
    const fmt = target % 1 === 0
      ? (v) => Math.round(v).toLocaleString()
      : (v) => v.toFixed(1);

    function frame(now) {
      const t = Math.min((now - start) / duration, 1);
      const eased = 1 - Math.pow(1 - t, 3);
      el.textContent = fmt(target * eased) + suffix;
      if (t < 1) requestAnimationFrame(frame);
    }
    requestAnimationFrame(frame);
  }

  /* ---------- IntersectionObserver: reveals + counters ---------- */
  function initReveal() {
    const reveals = document.querySelectorAll(".plc-reveal");
    const counters = document.querySelectorAll("[data-count]");
    if (!("IntersectionObserver" in window)) {
      reveals.forEach((r) => r.classList.add("is-in"));
      counters.forEach(animateCounter);
      return;
    }
    const io = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (!entry.isIntersecting) return;
          entry.target.classList.add("is-in");
          if (entry.target.matches("[data-count]")) animateCounter(entry.target);
          entry.target.querySelectorAll &&
            entry.target.querySelectorAll("[data-count]").forEach(animateCounter);
          io.unobserve(entry.target);
        });
      },
      { threshold: 0.18 }
    );
    reveals.forEach((r) => io.observe(r));
    counters.forEach((c) => io.observe(c));
  }

  /* ---------- Mini scan-cycle demo ---------- */
  // Inputs: Start (latching), Stop (momentary), Sensor (momentary)
  // Logic: Run := (Start OR Run) AND NOT Stop
  //        Lamp := Run
  //        Alarm := Run AND Sensor
  function initScanDemo() {
    const root = document.getElementById("plc-demo");
    if (!root) return;

    const state = { Start: false, Stop: false, Sensor: false, Run: false };

    const $ = (sel) => root.querySelector(sel);
    const lampRun   = $('[data-out="Run"]');
    const lampLamp  = $('[data-out="Lamp"]');
    const lampAlarm = $('[data-out="Alarm"]');
    const rung      = $('[data-rung]');
    const stepLabel = $('[data-step]');

    const btnStart  = $('[data-btn="Start"]');
    const btnStop   = $('[data-btn="Stop"]');
    const btnSensor = $('[data-btn="Sensor"]');

    function paint(step) {
      lampRun.classList.toggle("is-on", state.Run);
      lampLamp.classList.toggle("is-on", state.Run);
      lampAlarm.classList.toggle("is-on", state.Run && state.Sensor);
      btnStart.classList.toggle("is-pressed", state.Start);
      stepLabel.textContent = step;
    }

    function scan() {
      // 1. Read inputs (already in state)
      stepLabel.textContent = "1 · Read inputs";
      rung.textContent = `START=${+state.Start}  STOP=${+state.Stop}  SENSOR=${+state.Sensor}`;
      setTimeout(() => {
        // 2. Execute logic
        stepLabel.textContent = "2 · Execute logic";
        state.Run = (state.Start || state.Run) && !state.Stop;
        rung.textContent = `Run := (Start OR Run) AND NOT Stop  ⇒ ${+state.Run}`;
        setTimeout(() => {
          // 3. Update outputs
          stepLabel.textContent = "3 · Update outputs";
          paint("3 · Update outputs");
          // momentary inputs reset after the scan
          state.Stop = false;
          state.Sensor = false;
          btnStop.classList.remove("is-pressed");
          btnSensor.classList.remove("is-pressed");
        }, 350);
      }, 350);
    }

    btnStart.addEventListener("click", () => {
      state.Start = !state.Start;
      scan();
    });
    btnStop.addEventListener("click", () => {
      state.Stop = true;
      state.Start = false;
      btnStop.classList.add("is-pressed");
      scan();
    });
    btnSensor.addEventListener("click", () => {
      state.Sensor = true;
      btnSensor.classList.add("is-pressed");
      scan();
    });

    paint("Idle · press an input");
    rung.textContent = "Run := (Start OR Run) AND NOT Stop";
  }

  /* ---------- Progress tracker (localStorage) on roadmap ---------- */
  function initProgress() {
    const steps = document.querySelectorAll(".plc-step[data-sprint-id]");
    if (!steps.length) return;
    const KEY = "plc-fasttrack-progress-v1";
    let done = {};
    try { done = JSON.parse(localStorage.getItem(KEY) || "{}"); } catch (_) {}

    steps.forEach((step) => {
      const id = step.dataset.sprintId;
      if (done[id]) step.classList.add("is-done");
      step.addEventListener("click", (e) => {
        // Allow alt/middle-click to mark done without navigating
        if (e.altKey) {
          e.preventDefault();
          done[id] = !done[id];
          step.classList.toggle("is-done", !!done[id]);
          localStorage.setItem(KEY, JSON.stringify(done));
        }
      });
    });
  }

  ready(() => {
    initReveal();
    initScanDemo();
    initProgress();
  });
})();
