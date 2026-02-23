'use client';

import { useEffect, useState } from 'react';
import { useStreamSocket } from '../hooks/useStreamSocket';

export function VoiceTutorPanel() {
  const [transcript, setTranscript] = useState('Explain RC filter cutoff frequency');
  const { latestMessage, send } = useStreamSocket('ws://localhost:8000/api/v1/lab/ws/voice-tutor');

  useEffect(() => {
    if (!latestMessage) return;
  }, [latestMessage]);

  return (
    <section className="rounded-xl border border-violet-500/30 p-4">
      <h2 className="font-semibold">Voice Tutor</h2>
      <input className="mt-2 w-full bg-slate-900 p-2" value={transcript} onChange={(e) => setTranscript(e.target.value)} />
      <button className="mt-2 px-3 py-1 bg-violet-600 rounded" onClick={() => send(transcript)}>Stream Tutor</button>
      <p className="mt-2 text-sm text-slate-300">Live: {latestMessage ?? 'ready'}</p>
    </section>
  );
}
