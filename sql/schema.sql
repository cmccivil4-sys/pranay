CREATE TABLE organizations (
  id UUID PRIMARY KEY,
  name TEXT NOT NULL,
  type TEXT NOT NULL CHECK (type IN ('saas','college_offline')),
  created_at TIMESTAMPTZ DEFAULT now()
);

CREATE TABLE users (
  id UUID PRIMARY KEY,
  organization_id UUID REFERENCES organizations(id),
  email TEXT UNIQUE NOT NULL,
  password_hash TEXT NOT NULL,
  role TEXT NOT NULL CHECK (role IN ('student','instructor','admin')),
  created_at TIMESTAMPTZ DEFAULT now()
);

CREATE TABLE subscriptions (
  id UUID PRIMARY KEY,
  user_id UUID REFERENCES users(id),
  plan TEXT NOT NULL CHECK (plan IN ('free','student_monthly','student_yearly','campus')),
  status TEXT NOT NULL,
  renewal_at TIMESTAMPTZ,
  created_at TIMESTAMPTZ DEFAULT now()
);

CREATE TABLE credit_wallets (
  user_id UUID PRIMARY KEY REFERENCES users(id),
  balance INTEGER NOT NULL DEFAULT 0,
  updated_at TIMESTAMPTZ DEFAULT now()
);

CREATE TABLE notes (
  id UUID PRIMARY KEY,
  user_id UUID REFERENCES users(id),
  title TEXT NOT NULL,
  content TEXT NOT NULL,
  embedding VECTOR(768),
  created_at TIMESTAMPTZ DEFAULT now()
);

CREATE TABLE revision_cards (
  id UUID PRIMARY KEY,
  note_id UUID REFERENCES notes(id),
  question TEXT NOT NULL,
  answer TEXT NOT NULL,
  difficulty SMALLINT NOT NULL,
  created_at TIMESTAMPTZ DEFAULT now()
);

CREATE TABLE learning_attempts (
  id UUID PRIMARY KEY,
  user_id UUID REFERENCES users(id),
  topic TEXT NOT NULL,
  mistake_type TEXT,
  hesitation_ms INTEGER,
  score NUMERIC(5,2),
  created_at TIMESTAMPTZ DEFAULT now()
);

CREATE TABLE ai_feedback_events (
  id UUID PRIMARY KEY,
  user_id UUID REFERENCES users(id),
  module TEXT NOT NULL,
  feedback_score INTEGER,
  payload JSONB,
  created_at TIMESTAMPTZ DEFAULT now()
);

CREATE TABLE offline_licenses (
  id UUID PRIMARY KEY,
  organization_id UUID REFERENCES organizations(id),
  campus_code TEXT NOT NULL,
  public_claims JSONB NOT NULL,
  signature TEXT NOT NULL,
  expires_at TIMESTAMPTZ NOT NULL,
  created_at TIMESTAMPTZ DEFAULT now()
);
