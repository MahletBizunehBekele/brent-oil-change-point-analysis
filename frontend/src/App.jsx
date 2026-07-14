import "./App.css";
import FilterPanel from "./components/FilterPanel";
import PriceChart from "./components/PriceChart";
import EventTimeline from "./components/EventTimeline";

function App() {
  return (
    <div style={{ padding: "20px" }}>
      <h1>Brent Oil Dashboard</h1>

      <FilterPanel />

      <hr />

      <PriceChart />

      <hr />

      <EventTimeline />
    </div>
  );
}

export default App;