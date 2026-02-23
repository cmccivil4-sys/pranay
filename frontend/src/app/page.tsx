import { NotebookPlus } from '../components/NotebookPlus';
import { NumericalSolver } from '../components/NumericalSolver';
import { CircuitScanner } from '../components/CircuitScanner';
import { VirtualLabCanvas } from '../components/VirtualLabCanvas';
import { VoiceTutorPanel } from '../components/VoiceTutorPanel';
import { WeakConceptInsights } from '../components/WeakConceptInsights';

export default function HomePage() {
  return (
    <main className="min-h-screen bg-slate-950 text-slate-100 p-4 grid gap-4 md:grid-cols-2">
      <NotebookPlus />
      <VoiceTutorPanel />
      <NumericalSolver />
      <CircuitScanner />
      <VirtualLabCanvas />
      <WeakConceptInsights />
    </main>
  );
}
