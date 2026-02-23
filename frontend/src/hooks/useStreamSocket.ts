'use client';

import { useEffect, useRef, useState } from 'react';

export function useStreamSocket(url: string) {
  const [latestMessage, setLatestMessage] = useState<string | null>(null);
  const wsRef = useRef<WebSocket | null>(null);

  useEffect(() => {
    const ws = new WebSocket(url);
    ws.onmessage = (event) => setLatestMessage(event.data);
    wsRef.current = ws;
    return () => ws.close();
  }, [url]);

  const send = (payload: string) => wsRef.current?.send(payload);

  return { latestMessage, send };
}
