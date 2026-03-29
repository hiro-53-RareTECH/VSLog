def test_show_endpoints(app):
    print("\n=== registered endpoints ===")
    for rule in app.url_map.iter_rules():
        print(f"{rule.endpoint:40} {rule.methods} {rule.rule}")
