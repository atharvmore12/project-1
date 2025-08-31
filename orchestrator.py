# pseudocode

def main_cycle(target_url):
    # STEP 1: Recon
    urls, params = run_recon(target_url)
    save_to_file(urls, "data/discovered/urls.txt")

    # STEP 2: AI Reasoning
    attack_plan = ai_reasoner.analyze(urls, params)
    save_json(attack_plan, "data/attack_plans/latest.json")

    # STEP 3: Launch Attacks
    raw_results = attack_engine.execute(attack_plan)
    save_json(raw_results, "data/results/raw.json")

    # STEP 4: Verify Exploits
    confirmed_vulns = validator.confirm(raw_results)
    save_json(confirmed_vulns, "data/results/confirmed.json")

    # STEP 5: Generate Report
    report_path = reporter.generate(confirmed_vulns)
    slack_alert.send(f"New report: {report_path}")

    # STEP 6: Schedule Repeat (optional)
    if config.AUTO_REPEAT:
        schedule_next_run(delay_hours=24)
