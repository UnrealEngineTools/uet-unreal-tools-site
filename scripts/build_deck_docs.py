"""Build the static Deck Toolkit documentation using only Python's standard library."""
from pathlib import Path
import html, json, re

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'deck-toolkit'
BASE = '/deck-toolkit/'
R2 = 'https://pub-5f5c0d0b15df417e9653e1f4329e3269.r2.dev/ultimate-deck-building-toolkit-builds/0.3.0/'
EXAMPLE = R2 + 'UltimateDeckBuildingToolkit_Example_UE5.8.zip'
PAGES = []
def page(slug, title, summary, body):
    PAGES.append(dict(slug=slug,title=title,summary=summary,body=body))
def code(text, language='cpp'):
    return '<div class="code"><div class="code-label">'+language+'</div><pre><code>'+html.escape(text.strip())+'</code></pre><button class="copy" type="button" aria-label="Copy code example">Copy</button></div>'
def table(headings, rows):
    return '<div class="table-wrap" tabindex="0" role="region" aria-label="Reference table"><table><thead><tr>'+''.join('<th scope="col">'+x+'</th>' for x in headings)+'</tr></thead><tbody>'+''.join('<tr>'+''.join('<td>'+x+'</td>' for x in row)+'</tr>' for row in rows)+'</tbody></table></div>'
def figure(file, alt, caption):
    return f'<figure><a href="{BASE}assets/{file}" aria-label="Open full-size screenshot"><img src="{BASE}assets/{file}" width="1920" height="1080" alt="{alt}" loading="lazy"></a><figcaption>{caption}</figcaption></figure>'

page('', 'Build your next advantage.', 'The complete guide to Ultimate Deck Building Toolkit: author cards, assemble decks and connect the workflow to your Unreal game.', '''
<div class="pills"><span>Version 0.3.0</span><span>Unreal Engine 5.8</span><span>Windows x64</span><span>C++ + Blueprint APIs</span></div>
<p class="lead">A card-authoring workbench, a player-facing deck workshop and a seeded reference encounter. Learn each part independently, then connect the parts your game needs.</p>
<div class="actions"><a class="button" href="getting-started/">Start with the example <span aria-hidden="true">↗</span></a><a class="button secondary" href="api/">Browse the API</a></div>
'''+figure('workshop.jpg','Unreal Engine deck workshop showing named decks, collection cards and an energy curve','Actual Unreal Engine capture. The workshop uses native Slate widgets.')+'''
<h2 id="choose">Choose your workflow</h2>
<div class="cards"><a href="cards/"><span>01 / AUTHOR</span><h3>Create cards and decks</h3><p>Define costs, ordered effects, retain and exhaust flags in Data Assets.</p></a><a href="workbench/"><span>02 / INSPECT</span><h3>Follow each effect</h3><p>Deal a seeded hand, queue a card copy and step through reference combat.</p></a><a href="workshop/"><span>03 / INTEGRATE</span><h3>Build a player workshop</h3><p>Connect your collection and named decks through the native model interface.</p></a><a href="persistence/"><span>04 / KEEP</span><h3>Save deck compositions</h3><p>Configure local JSON persistence and handle failed loads without losing a file.</p></a></div>
<h2 id="included">What you get</h2><p>Full C++ plugin source, eight public UObject classes, one public Slate widget, card/deck asset types, seven reference effect types, 20 original example cards, deck validation, draw probability, named-deck persistence and optional live tracing. A separate C++ example project demonstrates the workshop and encounter.</p>
<h2 id="scope">Know the integration boundary</h2><aside><strong>Designed for C++ integration.</strong> The session and rules expose Blueprint functions. The Slate workshop model, visual customization and trace instrumentation require native C++.</aside><p>The combat session is a local one-player, one-enemy reference implementation. Supply your own production combat, collection ownership, progression, artwork and audio. Automatic GAS hooks, multiplayer, arbitrary card-rule graphs, card-instance upgrades, cloud synchronization and cross-engine replay are outside version 0.3.0.</p>
<h2 id="map">Documentation map</h2><p>Follow <a href="getting-started/">Getting started</a> for installation and the example, <a href="session/">Reference combat</a> for Blueprint/runtime flow, <a href="rules/">Deck rules</a> for validation, and <a href="tracing/">Live tracing</a> for host-game diagnostics. The <a href="troubleshooting/">troubleshooting guide</a> covers common integration problems.</p>
''')

page('getting-started','Your first deck, in Unreal.','Install the plugin, try the workbench and run the independent example project.', '''
<h2 id="requirements">Requirements</h2><ul><li>Unreal Engine 5.8 on Windows x64.</li><li>The Ultimate Deck Building Toolkit plugin, installed separately from its example.</li><li>Visual Studio 2022 with the Unreal C++ workload to compile the source plugin or example project.</li></ul><p>This release has been checked with the installed binary UE 5.8 toolchain. Other engine versions and platforms are not currently supported.</p>
<h2 id="install">Install the plugin</h2><ol><li>Once the Fab release is available, install it for UE 5.8 through your Fab library.</li><li>Open your project and enable <strong>Ultimate Deck Building Toolkit</strong> under <strong>Edit &gt; Plugins</strong>. Restart when prompted.</li><li>For a manually supplied source package, place its complete <code>UltimateDeckToolkit</code> folder at <code>YourProject/Plugins/UltimateDeckToolkit</code>, then build Development Editor with the editor closed.</li></ol><aside>The first Fab release was submitted on September 10, 2026 and was pending review when these docs were published. Documentation availability does not mean the store release is approved.</aside>
<h2 id="editor">Try the editor tools</h2><ol><li>Open <strong>Tools &gt; Deck Workbench</strong> in the Deck Building section.</li><li>Use the 20 built-in cards, seed 42, five-card opening hand, three energy and ten-card hand limit.</li><li>Select a card, click <strong>Queue</strong> and use <strong>Step effect</strong> to inspect its resolution.</li><li>Open <strong>Tools &gt; Deck Workshop Preview</strong> to try collection search and deck editing.</li></ol><p>Built-in workbench cards and the workshop preview are transient. Use saved Data Assets for durable card authoring, and the persistent example below for saved deck compositions.</p>
<h2 id="example">Download and compile the example</h2><p>The example ZIP contains only the example project source and configuration. It depends on the separately installed plugin.</p><p><a class="button" href="'''+EXAMPLE+'''">Download UE 5.8 example ZIP</a></p><ol><li>Extract to a short writable path, such as <code>C:/Examples/DeckToolkitExample</code>.</li><li>Install the plugin for UE 5.8, or place a separately obtained source copy in the example's <code>Plugins/UltimateDeckToolkit</code> folder.</li><li>Build <code>DeckToolkitValidationEditor</code> in Development Editor.</li><li>Open <code>DeckToolkitValidation.uproject</code> and choose Play Standalone.</li></ol>
'''+code("& 'C:/Program Files/Epic Games/UE_5.8/Engine/Build/BatchFiles/Build.bat' DeckToolkitValidationEditor Win64 Development '-Project=C:/Examples/DeckToolkitExample/DeckToolkitValidation.uproject' -WaitMutex",'powershell')+'''
<h2 id="play">Edit, equip, play</h2><p>Select a named deck, add owned cards and choose <strong>Use this deck</strong>. Close the workshop, then select <strong>Play active deck</strong>. The example starts a reference encounter with seed 42, 60 health for each combatant, three energy and five drawn cards per turn. Enemy attacks deal six base damage.</p><p>The example saves compositions in <code>Saved/DeckToolkit/DemoDecks.json</code>. Close and reopen the application to verify that deck names, contents and active selection survive. Combat state is not saved.</p>
'''+figure('encounter.jpg','Standalone Unreal reference encounter after playing a card','The example connects a selected deck to the included reference session.')+'''
<h2 id="controls">Controls</h2><p>In the workshop, use Tab/arrow keys or D-pad to navigate, Enter/gamepad A to activate, and Escape/gamepad B to close. The example also presents clickable controls. Keyboard and simulated gamepad events have been checked; physical-controller acceptance has not been verified.</p>
<h2 id="package">Package your own game</h2><p>Enable the plugin in your project and use the normal Unreal Windows packaging workflow. Keep card/deck assets referenced by your cooked project or explicitly manage them in your asset-loading policy. The Editor module is omitted from game builds; the Runtime and UI modules remain available. Test your collection mappings and saves in the packaged application.</p>
''')

page('cards','Author cards and decks.','Create persistent Data Assets and understand the exact reference-effect vocabulary.', '''
<h2 id="card">Create a card asset</h2><ol><li>In the Content Browser, create <strong>Miscellaneous &gt; Data Asset</strong> with class <code>DeckToolkitCard</code>.</li><li>Set a non-empty CardName, Description and EnergyCost.</li><li>Add entries to Effects in the order they should resolve.</li><li>Choose retain/exhaust flags and save the asset normally.</li></ol>
'''+table(['Field','Meaning'],[('<code>CardName</code>','Display name. Required and not whitespace-only.'),('<code>Description</code>','Author-supplied display text; it does not generate gameplay rules.'),('<code>EnergyCost</code>','Integer from 0 to 1,000,000.'),('<code>bRetain</code>','Keep this copy in hand at turn end if it has not been played.'),('<code>bExhaust</code>','After resolving, move this copy to the exhaust pile instead of discard.'),('<code>Effects</code>','Ordered array of up to 64 FDTCardEffect entries. An empty array is valid.')])+'''
<h2 id="effects">Reference effect types</h2>
'''+table(['Type','Target and behavior'],[('Damage','Damage the enemy. Add player Strength, apply enemy Vulnerable, absorb with Block, then reduce Health.'),('Block','Add player block; cleared when the next player turn begins.'),('Heal','Restore player health, capped by MaxHealth.'),('GainEnergy','Increase current energy.'),('Draw','Draw player cards until the requested amount, hand limit or available cards are exhausted.'),('Strength','Add an encounter-long player damage bonus to each hit.'),('Vulnerable','Add enemy vulnerable turns. Damage is multiplied by 1.5 and rounded down.')])+'''
<p>Amounts are nonnegative integers up to 1,000,000. Additive reference values are bounded. Vulnerable ages on EndTurn. These are fixed reference semantics, not a configurable target system.</p>
<h2 id="conditions">Ordered effects and conditions</h2><p><code>EDTCardCondition::Always</code> always resolves. <code>TargetDefeated</code> resolves only when the reference enemy is already at zero health. The condition is evaluated when that effect executes. Effects after a lethal hit still run, allowing on-kill rewards.</p><p>For a card that deals damage and draws only on a kill, add Damage first, then Draw with TargetDefeated. Reversing the order changes the result. Damage itself expands into separate strength, vulnerable, block and health trace entries.</p>
<h2 id="deck">Create an authored deck</h2><p>Create a Data Asset of class <code>DeckToolkitDeck</code> and assign card asset references to <code>Cards</code>. Duplicate references represent separate playable copies. Authored order is preserved on loading; Initialize then performs the seeded shuffle. A session assigns each copy its own InstanceId.</p><p>A deck asset is distinct from a player's named-deck JSON entry: the asset references card objects; the workshop composition stores your catalog's string IDs. Your host resolves those IDs to definitions before starting combat.</p>
<h2 id="validation">Validate before simulation</h2><p><code>ValidateDefinition(FText&amp; OutReason)</code> checks names, costs, effect counts, enum values and amounts. Editor asset validation calls the same checks. Initialize validates every referenced card before replacing session state. A missing or invalid card rejects the complete reset.</p>
<h2 id="examples">Built-in examples</h2><p><code>UDeckToolkitExamples::CreateExampleCards(Outer)</code> returns 20 original transient definitions. They are useful for experimentation and tests; editing them does not create saved assets. Create your own Data Assets to preserve authoring changes.</p>
''')

page('workbench','See every effect resolve.','Use the editor workbench to author cards and inspect the seeded reference model.', '''
<h2 id="open">Open and load</h2><p>Choose <strong>Tools &gt; Deck Workbench</strong>. It initially loads the 20 original example definitions. To use your assets, select a deck asset or several card assets in the Content Browser and choose <strong>Load selected deck/cards</strong>.</p><p>A selected deck takes precedence. If multiple decks are selected, the first by asset path is used. Selected individual cards are sorted by asset path; an authored deck preserves its Cards array order.</p>
'''+figure('workbench.jpg','Deck Workbench with reference card definitions, hand controls and effect trace','The workbench runs the reference rules independently of your host game.')+'''
<h2 id="reset">Edit and reset</h2><p>Select a card in the deck list to inspect or edit its definition. Save persistent assets using Unreal's normal asset Save workflow. <strong>Reset &amp; deal</strong> snapshots current definitions and deals a new seeded hand. Editing an asset does not change a simulation already in progress; reset to test the new definition.</p>
<h2 id="step">Play or step</h2><ol><li><strong>Play</strong> resolves the selected card copy immediately.</li><li><strong>Queue</strong> spends its cost and reserves that instance for resolution.</li><li><strong>Step effect</strong> executes the next authored effect. One effect may produce multiple diagnostic trace entries.</li><li>Finish the pending card before playing another card or ending the turn.</li><li><strong>End turn / enemy attacks 6</strong> discards non-retained cards, attacks, ages vulnerable and begins the next turn when both combatants survive.</li></ol>
<h2 id="trace">Read the trace</h2><p>Inspect the sequence number, card instance, stage, detail and before/after values. The workbench uses the session's bounded 512-entry history. For a damage card, follow the value from base damage through Strength, Vulnerable, Block and Health. Rejected plays explain why and do not spend energy or move cards.</p>
<h2 id="seed">Reproduce a case</h2><p>Record the engine version, seed, ordered input deck, definitions, hand limit and commands. Reset with the same inputs to reproduce draws within the tested engine version, including reshuffles. Changing deck order or consuming commands in a different order changes the random stream. This is not a serialized encounter replay or a guarantee across engine versions.</p>
<h2 id="host">Inspect your host game separately</h2><p>The workbench does not execute arbitrary abilities or observe your game's combat automatically. Use the <a href="../tracing/">live trace bridge</a> for explicit instrumentation of your own implementation.</p>
''')

page('session','Run reference combat.','Drive the Blueprint-callable session without a world, widget or host-game dependency.', '''
<h2 id="lifecycle">Session lifecycle</h2><div class="flow" aria-label="Session flow"><span>Initialize</span><b>→</b><span>BeginTurn</span><b>→</b><span>Play / Queue + Step</span><b>→</b><span>EndTurn</span></div><p>Create a <code>UDeckToolkitSession</code> and retain it on a live host object. Initialize accepts 1 to 1,000 card definitions, a seed and a hand limit from 1 to 100. It validates atomically, snapshots each distinct definition, gives each copy a unique instance ID and shuffles.</p>
<h2 id="blueprint">Blueprint flow</h2><ol><li>Use <strong>Construct Object from Class</strong> with DeckToolkitSession and store its return value in a variable.</li><li>Call Initialize with Cards, Seed and HandLimit. Check its return value and OutReason.</li><li>Bind OnChanged to a UI refresh event. Query GetHand, GetEnergy and combat states.</li><li>Call BeginTurn with DrawCount and TurnEnergy.</li><li>Use the selected hand entry's InstanceId with PlayCard. Show OutReason when it returns false.</li><li>Call EndTurn, then BeginTurn for the next turn only if the session is not finished.</li></ol><aside>OnChanged handlers may read the session. Mutating calls from inside a notification are rejected. Schedule subsequent commands after the notification returns.</aside>
<h2 id="cpp">Minimal C++ call sequence</h2><p>Inside a live UObject host, retain the session in a UPROPERTY field. The following is an integration excerpt, not a complete actor class.</p>
'''+code('''// Host header (after including DeckToolkitSession.h):
UPROPERTY()
TObjectPtr<UDeckToolkitSession> Session;

// Host method (include DeckToolkitExamples.h in your .cpp):
Session = NewObject<UDeckToolkitSession>(this);
TArray<UDeckToolkitCard*> Cards = UDeckToolkitExamples::CreateExampleCards(this);
FText Reason;
if (Session->Initialize(Cards, 42, 10, Reason))
{
    Session->BeginTurn(5, 3);
    const TArray<FDTCardInstance> Hand = Session->GetHand();
    if (!Hand.IsEmpty())
    {
        // Inspect the boolean and Reason; a card can cost more than available energy.
        const bool bPlayed = Session->PlayCard(Hand[0].InstanceId, Reason);
    }
}''')+'''
<h2 id="turns">Turn boundaries</h2><p>BeginTurn requires an initialized, unfinished session with no active turn or pending card. It refreshes energy, clears player block and draws. DrawCount must be 0 to 1,000; TurnEnergy must be 0 to 1,000,000. EndTurn discards non-retained cards, optionally applies an enemy attack and ages vulnerable. The API does not automatically begin the next turn.</p>
<h2 id="queue">Queue and step</h2><p>QueueCard validates the instance and energy, spends the cost and removes that copy from the hand into pending resolution. StepEffect advances one authored effect. The resolving copy cannot be drawn during its own Draw effect. When resolution completes it enters discard or exhaust. PlayCard performs the equivalent complete resolution synchronously.</p>
<h2 id="piles">Draws and piles</h2><p>When draw is empty, discard is shuffled into draw. Exhausted and resolving copies are excluded. At the hand limit, undrawn cards stay in the draw pile. Retained cards occupy hand slots next turn. Both combatants begin at 60 Health and MaxHealth; the reference model exposes snapshots for reading, not general-purpose combatant configuration.</p>
<h2 id="events">Read state and events</h2><p>GetHand returns instance/definition pairs. GetDrawCount, GetDiscardCount and GetExhaustCount return pile sizes. GetPlayer/GetEnemy return FDTCombatState; IsResolving, IsTurnActive and IsFinished describe lifecycle. GetTrace returns recent FDTTraceEntry records. Treat returned values as snapshots and render from OnChanged, rather than polling every frame.</p>
''')

page('rules','Validate a composition.','Apply game-supplied deck constraints and measure opening-hand consistency.', '''
<h2 id="context">Supply the context</h2><p><code>UDeckToolkitRules::CheckAddCard</code> is a pure validation utility. It never queries an inventory singleton or player progression service. Fill FDTDeckAddContext with the current deck size/capacity, copies already present/copy limit, owned copies, player/required levels and whether class policy permits this card.</p>
'''+code('''FDTDeckAddContext Context;
Context.DeckSize = 12;
Context.Capacity = 20;
Context.CopiesInDeck = 1;
Context.CopyLimit = 3;
Context.OwnedCopies = 2;
Context.PlayerLevel = 5;
Context.RequiredLevel = 3;
Context.bClassAllowed = true;
const FDTDeckRuleResult Result = UDeckToolkitRules::CheckAddCard(Context);
// C++: Result.IsAllowed(). Blueprint: compare Failure with None.
// Use Result.Reason or map Failure to your own localized message.''')+'''
<h2 id="precedence">Rejection precedence</h2>
'''+table(['Order / failure','Condition'],[('1 / InvalidInput','Negative scalar input or CopiesInDeck greater than DeckSize.'),('2 / Capacity','DeckSize is already at Capacity.'),('3 / CopyLimit','CopiesInDeck has reached CopyLimit.'),('4 / Ownership','No additional owned copy is available.'),('5 / Level','PlayerLevel is below RequiredLevel.'),('6 / ClassRestriction','bClassAllowed is false.'),('None','The add is allowed by these supplied constraints.')])+'''
<p>A successful add check is not a complete deck legality check. Validate any minimum size, required card mix, faction rules or game-specific restrictions before equipping or starting combat.</p>
<h2 id="workshop">Workshop policies</h2><p>The default workshop maps deck size, copy, ownership and level values into this context. Its Family filter is a browsing filter; it does not enforce a deck class restriction. Add your own class policy in the host adapter's Add implementation, using CheckAddCard with bClassAllowed set explicitly. CanAdd on the base model is not virtual; customize the UI preflight too if you need to display that additional restriction before activation.</p>
<h2 id="probability">Opening-hand probability</h2><p><code>OpeningHandProbability(N, K, DrawCount)</code> gives the probability of at least one matching card in a draw without replacement: <code>1 - C(N-K, DrawCount) / C(N, DrawCount)</code>, with impossible-miss cases handled directly. For 20 cards, 3 matches and 5 draws, the chance is approximately <strong>60.09%</strong>.</p><p>Valid inputs require 0 ≤ K ≤ N ≤ 1,000,000 and 0 ≤ DrawCount ≤ N. Invalid inputs return -1. No matching cards or no draws returns 0. Drawing more than the number of non-matches returns 1.</p><aside>This measures draw consistency, not combat balance. It does not model mulligans, search effects, a draw policy, opponent strategy or win rates.</aside>
''')

page('workshop','Connect the player workshop.','Integrate the native Slate UI with your own catalog, ownership and deck model.', '''
<h2 id="model">Own and retain the model</h2><p><code>SDeckToolkitWorkshop</code> reads a <code>UDeckToolkitWorkshopModel</code> through a weak pointer. Your host must retain the UObject with UPROPERTY, or an appropriate FGCObject in an editor host. A raw pointer or Slate shared pointer alone does not keep a UObject alive.</p><p>Populate Catalog, Decks, ActiveDeck, Capacity and PlayerLevel before opening the widget. Call LoadExamples only for a disposable sample: it resets the model's catalog and deck list. A newly created base model does not populate itself.</p>
'''+code('''// Retain in your host's header:
UPROPERTY()
TObjectPtr<UDeckToolkitWorkshopModel> WorkshopModel;

// In a host method, after including DeckToolkitWorkshop.h:
WorkshopModel = NewObject<UDeckToolkitWorkshopModel>(this);
WorkshopModel->LoadExamples(); // Sample data only.
TSharedRef<SDeckToolkitWorkshop> Workshop =
    SNew(SDeckToolkitWorkshop).Model(WorkshopModel.Get());
// Attach Workshop to your host's viewport or Slate container.
// Retain/remove the Slate content and restore input focus when it closes.''')+'''
<h2 id="catalog">Map your collection</h2>
'''+table(['Type','Fields / responsibility'],[('FDTWorkshopCard','Id, Name, Description, Family, Rarity, Cost, Owned, CopyLimit, RequiredLevel. Presentation data supplied by your game.'),('FDTWorkshopDeck','Id (FGuid), Name and ordered Cards (string IDs, including duplicates).'),('Model state','Catalog, Decks, ActiveDeck, Capacity (default 20), PlayerLevel (default 1).')])+'''
<p>Use stable catalog IDs that survive display-name changes. The sample uses card names as IDs for simplicity; a production catalog should have a deliberate migration strategy. IDs map to your own card definitions and are not automatically converted to Data Asset paths.</p>
<h2 id="adapters">Override the adapter boundary</h2><p>Subclass the model and override Refresh, Add, Remove, Create, RenameDeck, Delete, Equip and Save as needed. Refresh can fetch your host's current collection snapshot. Add should validate your rules and return a user-facing reason on failure. Keep updates on the game thread. Method names and signatures are listed in the <a href="../api/">API reference</a>.</p><p>Base-model modifications are in memory; its Save returns a transient-session message. The persistent subclass supplies local file storage. Calling a model mutation directly from C++ does not automatically call Save; explicitly save when bypassing the widget workflow.</p>
<h2 id="selection">Editing is separate from equipping</h2><p>Selecting a named deck changes the editing target. <strong>Use this deck</strong> calls Equip and changes ActiveDeck. SelectDeck changes the widget's editing deck; GetEditingDeck reads it. Deleting the active deck selects the first remaining deck, or leaves no active deck if the list is empty.</p>
<h2 id="ui">Presentation and input</h2><p>Search matches collection text including name, description, rarity and cost; Family chips filter the visible collection. Capacity, average energy and the cost curve update during editing. The widget has an OnClosed delegate, SelectCard and SetStatus for host coordination.</p><p>Integrate focus and input mode in your owning controller. The example source, <code>Source/DeckToolkitValidation/DeckToolkitDemo.cpp</code>, demonstrates viewport hosting and the transition to the encounter. The provided UI is Slate; Blueprint-configurable themes and UMG adapters are not included. Modify the native presentation for your game.</p>
<h2 id="cook">Resolve compositions for combat</h2><ol><li>Read the model's ActiveDeck ID and find that named deck.</li><li>Resolve every string card ID against your current catalog/definition map.</li><li>Reject or repair unknown definitions and validate your complete deck rules.</li><li>Build an ordered array of card definition pointers, preserving duplicate IDs.</li><li>Initialize the reference session, or hand the composition to your production combat system.</li></ol>
''')

page('persistence','Keep the decks you build.','Configure local JSON persistence, understand the file format and recover from failed saves.', '''
<h2 id="configure">Configure after catalog setup</h2><p>Use UDeckToolkitPersistentWorkshopModel when you want local file persistence. Populate the host-supplied catalog and default decks first, then call ConfigureFile. Retain the model for the life of the workshop. A missing file keeps defaults and permits future saves.</p>
'''+code('''// Includes: DeckToolkitPersistentWorkshop.h and Misc/Paths.h
// Model must also be retained by your host in a UPROPERTY field.
UDeckToolkitPersistentWorkshopModel* Model =
    NewObject<UDeckToolkitPersistentWorkshopModel>(this);
Model->LoadExamples(); // Replace with your production catalog/defaults.
FText Status;
const FString Filename = FPaths::ProjectSavedDir() / TEXT("DeckToolkit/PlayerDecks.json");
const bool bConfigured = Model->ConfigureFile(Filename, Status);
// Show Status. Do not treat false as permission to overwrite the original.
// For programmatic mutations, call Model->Save(Status) explicitly.''')+'''
<h2 id="schema">Schema version 1</h2><p>The file contains compositions and active selection. It does not save catalog definitions, owned-copy counts, progression, combat state, random-stream state or card-instance upgrades.</p>
'''+code('''{
  "schemaVersion": 1,
  "activeDeckId": "e6d7dd91-27fb-480c-92be-e58fe0ae01ea",
  "decks": [
    {
      "id": "e6d7dd91-27fb-480c-92be-e58fe0ae01ea",
      "name": "Starter",
      "cards": ["strike", "strike", "guard"]
    }
  ]
}''','json')+'''
<p>The IDs in this example are illustrative: populate matching catalog entries in your host. GUIDs use the standard digits-with-hyphens format. Each deck ID must be valid and unique. If decks exist, activeDeckId must identify one of them. An empty collection may use an empty activeDeckId string.</p>
<h2 id="limits">File limits</h2>
'''+table(['Limit','Value'],[('Encoded JSON file','4 MiB maximum'),('Named decks','128 maximum'),('Cards in one saved deck','512 maximum; separate from your gameplay capacity'),('Deck name','Non-blank, at most 48 characters'),('Card ID','Non-empty string, at most 512 characters'),('Schema','Exactly version 1')])+'''
<h2 id="load">Transactional loading</h2><p>The complete file is parsed and validated before Decks and ActiveDeck change. Invalid, oversized or future-schema files preserve memory and disable writes. Unknown catalog IDs are deliberately retained so the player can remove or repair them. Syntactically valid compositions can still violate your current ownership or gameplay rules; validate those before use.</p>
<h2 id="save">Recoverable replacement</h2><p>Save validates the model, writes a unique temporary sibling, then moves the previous primary file to a .backup sibling while installing the new file. A successful save removes the backup. On failure it attempts to restore the previous primary. ConfigureFile can restore a backup if the primary is missing. This reduces replacement risk but is not a power-loss durability guarantee.</p>
<h2 id="recovery">Handle a failure</h2><ol><li>Display Status and preserve the primary file and any .backup sibling.</li><li>For a transient write failure, keep the model alive and use <strong>Save / Retry</strong>; edits remain in memory.</li><li>For a malformed or future-schema load, resolve the file or configure a different valid supported file. Do not silently replace the rejected file with defaults.</li><li>For unresolved backup recovery, restore access and configure the file again before writing.</li></ol><p>Use one writer per file. Concurrent processes, cross-device sync and conflict resolution are not implemented. Store saves in a writable per-user location; do not use the installed plugin directory.</p>
'''+figure('persistence.jpg','Named deck selected independently from the active deck in the standalone sample','The sample exercises named decks, active selection and fresh-process reload.')+'''
<h2 id="migration">Evolve your catalog</h2><p>Keep stable IDs or perform a host-controlled migration before enabling writes. Do not increase schemaVersion and expect version 0.3.0 to read it. Preserve old player files during migration and test missing definitions, removed cards and changed deck policies against the new catalog.</p>
''')

page('tracing','Trace your own combat.','Feed observed events into a bounded, opt-in local diagnostic history.', '''
<h2 id="difference">Two different traces</h2><p>The reference session produces its own 512-entry effect log. The live trace bridge is a separate world subsystem for events observed in your actual game. It does not intercept GAS, calculate damage or automatically connect the reference session to a host.</p>
<h2 id="instrument">Instrument a play</h2><ol><li>Find the subsystem with <code>UDeckToolkitLiveTrace::Find(WorldContext)</code>; handle a null result.</li><li>Enable capture for the diagnostic session.</li><li>Call BeginCard once to obtain a local PlayId.</li><li>Pass that GUID through synchronous and delayed work belonging to the play.</li><li>Call Record or RecordValue with your observed stage, detail and optional target.</li></ol>
'''+code('''// Includes: DeckToolkitLiveTrace.h
// CardObject, SourceActor and TargetActor are supplied by your host game.
if (UDeckToolkitLiveTrace* Trace = UDeckToolkitLiveTrace::Find(this))
{
    const FGuid PlayId = Trace->BeginCard(CardObject, TEXT("Strike"), SourceActor, TargetActor);
    Trace->Record(PlayId, TEXT("Queued"), TEXT("Host accepted the play"));
    // After your own combat code applies the effect:
    Trace->RecordValue(PlayId, TEXT("Health"), HealthBefore, HealthAfter,
        TEXT("Observed enemy health"), TargetActor);
}''')+'''
<p>This excerpt requires the host variables named in the comments. The bridge only records supplied values. Find, BeginCard, Record and RecordValue are native C++ functions; only GetEvents and Clear are exposed as Blueprint functions.</p>
<h2 id="capture">Enable capture and inspect</h2><p>Open <strong>Tools &gt; Live Card Trace</strong>, start PIE and enable capture. Select the correct world when multiple PIE/game worlds exist. In a development console, use:</p>
'''+code('''DeckToolkit.Trace 1
DeckToolkit.ExportTrace
DeckToolkit.Trace 0''','console')+'''
<p>Export writes JSON under <code>Saved/DeckToolkit/LiveTrace-&lt;guid&gt;.json</code>. Native code can use ExportJson(Filename) and check its boolean result. Do not rely on an interactive console being available in every Shipping configuration; integrate native controls if your product needs them.</p>
<h2 id="fields">Event fields</h2><p>FDTLiveTraceEvent records PlayId, Sequence, TimeSeconds, Card, Source, Target, Stage and Detail. RecordValue additionally sets Before, After and bHasValues. GetRevision changes as history changes and can help avoid rebuilding an inspector unnecessarily.</p>
<h2 id="bounds">Lifetime and limits</h2><p>Capture defaults off. The subsystem does not tick, replicate or retain strong actor references. History is bounded to 2,048 events and 512 play metadata records. Disabled capture makes BeginCard return an invalid GUID and drops new records. Clear removes events and metadata; later events for cleared or evicted plays are discarded. Start a new play capture after clearing.</p><p>Use calls on the game thread. Only the open editor inspector polls. This is local observed history, not multiplayer telemetry or a replay system. Choose diagnostic labels appropriate for any JSON you intend to share.</p>
''')

page('api','Find the API you need.','Public types, native integration methods, Blueprint access and module dependencies for version 0.3.0.', '''
<h2 id="modules">Modules and includes</h2>
'''+table(['Module','Purpose','Public headers'],[('DeckToolkitRuntime / Runtime','Assets, session, rules, examples and live tracing','DeckToolkitCard.h, DeckToolkitExamples.h, DeckToolkitSession.h, DeckToolkitRules.h, DeckToolkitLiveTrace.h'),('DeckToolkitUI / Runtime','Native Slate workshop and optional persistence','DeckToolkitWorkshop.h, DeckToolkitPersistentWorkshop.h'),('DeckToolkitEditor / Editor','Workbench, preview and trace inspector','Editor implementation; omit from runtime dependencies')])+'''
<p>Add modules to your host's Build.cs according to where their types are used. Public headers that expose toolkit types need public dependencies; implementation-only use can use private dependencies. For a native workshop host, the following is a typical implementation dependency list:</p>
'''+code('''PrivateDependencyModuleNames.AddRange(new string[] {
    "DeckToolkitRuntime", "DeckToolkitUI", "Slate", "SlateCore"
});''','csharp')+'''
<p>The plugin uses standard Unreal modules including Core, CoreUObject, Engine, Slate, InputCore and Json. It has no additional marketplace plugin, GAS or external-service dependency. All three modules currently allow Win64 only.</p>
<h2 id="assets">Assets and examples</h2>
'''+table(['Type / method','Access and purpose'],[('UDeckToolkitCard','Blueprint asset type; CardName, Description, EnergyCost, bRetain, bExhaust, Effects.'),('ValidateDefinition(FText&amp;) const','Native validation; returns bool and failure text.'),('UDeckToolkitDeck::Cards','Blueprint-visible authored array of card references.'),('UDeckToolkitExamples::CreateExampleCards(UObject*)','Returns TArray&lt;UDeckToolkitCard*&gt;; original transient definitions.')])+'''
<h2 id="session">UDeckToolkitSession</h2>
'''+table(['Function','Result / Blueprint access'],[('Initialize(const TArray&lt;UDeckToolkitCard*&gt;&amp;, int32 Seed, int32 HandLimit, FText&amp;)','bool; callable. Atomic reset and snapshot.'),('BeginTurn(int32 DrawCount, int32 TurnEnergy)','bool; callable.'),('EndTurn(int32 EnemyDamage = 0)','bool; callable. Does not begin another turn.'),('CanPlayCard(int32 InstanceId, FText&amp;) const','bool; pure.'),('QueueCard(int32 InstanceId, FText&amp;)','bool; callable. Reserve copy and spend energy.'),('StepEffect() / PlayCard(int32 InstanceId, FText&amp;)','bool; callable. Advance pending resolution / resolve a play.'),('GetHand()','TArray&lt;FDTCardInstance&gt;; pure.'),('GetDrawCount / GetDiscardCount / GetExhaustCount / GetEnergy','int32; pure, no arguments.'),('IsResolving / IsTurnActive / IsFinished','bool; pure, no arguments.'),('GetPlayer / GetEnemy','FDTCombatState; pure, no arguments.'),('GetTrace()','TArray&lt;FDTTraceEntry&gt;; pure.'),('OnChanged','Blueprint-assignable multicast delegate; handlers must not mutate the session.')])+'''
<h2 id="rules">UDeckToolkitRules</h2><p><code>CheckAddCard(const FDTDeckAddContext&amp;)</code> returns FDTDeckRuleResult. <code>OpeningHandProbability(int32 DeckSize, int32 MatchingCards, int32 DrawCount)</code> returns double. Both are static Blueprint-pure functions. Result.IsAllowed() is a native helper; Blueprint callers compare Failure with None.</p>
<h2 id="workshop">Native workshop API</h2>
'''+table(['UDeckToolkitWorkshopModel method','Signature / result'],[('Refresh','virtual void Refresh()'),('Add','virtual bool Add(FGuid Deck, const FString&amp; Card, FText&amp; Reason)'),('Remove','virtual bool Remove(FGuid Deck, const FString&amp; Card)'),('Create','virtual FGuid Create(const FString&amp; Name)'),('RenameDeck','virtual void RenameDeck(FGuid Deck, const FString&amp; Name)'),('Delete / Equip','virtual void Delete(FGuid Deck) / Equip(FGuid Deck)'),('Save','virtual bool Save(FText&amp; Status)'),('CanAdd','bool CanAdd(FGuid Deck, const FString&amp; Card, FText&amp; Reason) const; non-virtual'),('LoadExamples','void LoadExamples(); replaces catalog and decks')])+'''
<p><code>UDeckToolkitPersistentWorkshopModel</code> adds <code>bool ConfigureFile(const FString&amp; Filename, FText&amp; Status)</code>, overrides Save and provides <code>const FString&amp; GetSavePath() const</code>. These methods are native, not Blueprint-callable.</p><p><code>SDeckToolkitWorkshop</code> takes Model and OnClosed Slate arguments. Public helpers: <code>FGuid GetEditingDeck() const</code>, <code>void SelectDeck(FGuid)</code>, <code>void SelectCard(const FString&amp;)</code>, and <code>void SetStatus(const FText&amp;)</code>.</p>
<h2 id="trace">UDeckToolkitLiveTrace</h2>
'''+table(['Method','Access / result'],[('Find(const UObject* WorldContext)','Native static; subsystem pointer or null.'),('IsCaptureEnabled / SetCaptureEnabled(bool)','Native static capture controls.'),('BeginCard(const UObject* Card, const FString&amp; Name, const AActor* Source, const AActor* Target)','Native; FGuid.'),('Record(FGuid, FName Stage, const FString&amp; Detail, const AActor* Target = nullptr)','Native; void.'),('RecordValue(FGuid, FName Stage, double Before, double After, const FString&amp; Detail, const AActor* Target = nullptr)','Native; void.'),('GetEvents() const / Clear()','Blueprint-pure event array / Blueprint-callable void.'),('GetRevision() const / ExportJson(const FString&amp;) const','Native int64 / bool.')])+'''
<h2 id="structs">Value types</h2><p>FDTCardEffect: Type, Amount, Condition. FDTCardInstance: InstanceId, Definition. FDTCombatState: Health, MaxHealth, Block, Strength, VulnerableTurns. FDTTraceEntry: Sequence, CardInstanceId, Stage, Detail, Before, After. See <a href="../tracing/#fields">live event fields</a> and <a href="../workshop/#catalog">workshop presentation types</a> for the remaining records.</p>
''')

page('troubleshooting','Get back to building.','Resolve common setup, integration and save issues, and understand what has been verified.', '''
<h2 id="modules">Missing modules or failed load</h2><p>Confirm the engine is UE 5.8 and the plugin is enabled. For a manual source install, check the folder is Plugins/UltimateDeckToolkit with the descriptor directly inside it. Close the editor, generate/build the C++ project with the Unreal C++ toolchain, and inspect the first compiler error. The example also requires its own C++ module to be built.</p>
<h2 id="empty">Empty workshop or disappearing model</h2><p>Populate the catalog/default decks before constructing the widget. Use LoadExamples only for a sample. Retain the model in a UPROPERTY or FGCObject; the widget stores a weak pointer. Keep IDs stable and unique in your catalog, and resolve saved IDs against current definitions. The base Refresh method is empty: your adapter supplies external collection refresh behavior.</p>
<h2 id="play">A card cannot be played</h2><p>Read OutReason. A play needs an active, unfinished turn, enough energy, the selected InstanceId in hand and no other pending resolution. Use the copy's InstanceId, not a card asset ID or hand-array index. Finish a queued card before starting another command. Do not mutate from an OnChanged callback.</p>
<h2 id="edits">Card edits are not affecting the encounter</h2><p>Initialize snapshots definitions. Reset and deal after editing to start a new session with updated data. Save persistent assets normally; built-in example objects are transient. Workshop JSON stores compositions, not card definitions.</p>
<h2 id="save">Deck changes are not saved</h2><p>The editor Workshop Preview uses the transient base model. Use the persistent model or standalone example for durable saves. Configure the file after catalog setup, show the returned status and use a writable user path. If you mutate a model directly, call Save explicitly. For malformed files and .backup recovery, follow the <a href="../persistence/#recovery">recovery workflow</a>.</p>
<h2 id="equipped">The wrong deck starts combat</h2><p>The editing selection is independent of ActiveDeck. Choose Use this deck, save the model and resolve the deck identified by ActiveDeck. Your host needs to convert each card ID to its current definition and validate the resulting complete composition.</p>
<h2 id="trace">The live trace is empty</h2><p>Enable capture, select the correct PIE/game world and instrument BeginCard plus Record/RecordValue in your host. Capture has no automatic GAS hooks. Do not reuse a GUID from before Clear or after its metadata was evicted. A disabled BeginCard call produces an invalid GUID.</p>
<h2 id="performance">Does this add runtime overhead?</h2><p>The Editor module is excluded from packaged games. Runtime code has cost when used, including a visible Slate workshop and explicit diagnostic recording. The session and live trace subsystem do not tick, and capture defaults off. The open editor trace inspector polls. Measure your actual catalog size, UI changes and host integration on your target hardware; editor-only functionality does not imply that every component is free at runtime.</p>
<h2 id="tested">Validation and limits</h2><ul><li>UE 5.8 strict BuildPlugin passed for Windows Editor, Development and Shipping.</li><li>Fourteen automated checks passed in a clean project, covering rules, seeded sessions, traces, persistence and workshop behavior.</li><li>The standalone example passed a two-process save/load check.</li><li>Keyboard and simulated gamepad input checked. Physical controllers, other platforms and engine versions have not been verified.</li></ul><p>Run included checks from Session Frontend &gt; Automation, filtering for DeckToolkit. Presentation checks require a graphics device and may open preview windows; use a separate test project.</p>
<h2 id="support">Prepare a useful issue report</h2><p>When contacting the publisher through the available Fab support channel, include UE and plugin versions, Windows version, the exact steps, expected/actual behavior and the first relevant error. For draw issues include seed and ordered definitions; for save issues preserve the original JSON and backup locally. Share only the diagnostic data needed for the issue.</p>
<h2 id="release">Version 0.3.0</h2><p>This documentation describes the initial submitted feature set: card/deck Data Assets, seeded reference combat, ordered effects, rules/probability helpers, a native workshop, local named-deck saves and explicit host trace instrumentation. No multiplayer, cloud sync, automatic balance predictions, arbitrary rule graphs, UMG theme kit or automatic GAS adapter is included.</p>
''')

def url(p): return BASE + (p['slug']+'/' if p['slug'] else '')
OUT.mkdir(exist_ok=True)
search=[]
for i,p in enumerate(PAGES):
    headings=re.findall(r'<h2 id="([^"]+)">([^<]+)</h2>',p['body'])
    nav=''.join(f'<a href="{url(q)}"'+(' aria-current="page"' if q is p else '')+f'><span>{j+1:02d}</span>{html.escape("Overview" if j==0 else {"getting-started":"Getting started","cards":"Cards & decks","workbench":"Editor workbench","session":"Reference combat","rules":"Deck rules","workshop":"Workshop integration","persistence":"Persistence","tracing":"Live tracing","api":"API reference","troubleshooting":"Troubleshooting"}[q["slug"]])}</a>' for j,q in enumerate(PAGES))
    toc=''.join(f'<a href="#{key}">{label}</a>' for key,label in headings)
    prev=f'<a href="{url(PAGES[i-1])}"><small>PREVIOUS</small>{PAGES[i-1]["title"]}</a>' if i else '<a href="/"><small>UNREAL TOOLS</small>Explore the toolbox</a>'
    nxt=f'<a href="{url(PAGES[i+1])}"><small>NEXT</small>{PAGES[i+1]["title"]} →</a>' if i+1<len(PAGES) else f'<a href="{BASE}"><small>OVERVIEW</small>Back to the guide →</a>'
    doc=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{html.escape(p['title'])} | Deck Toolkit | Unreal Tools</title><meta name="description" content="{html.escape(p['summary'],quote=True)}"><link rel="canonical" href="https://www.unrealtools.com{url(p)}"><meta name="theme-color" content="#09090c"><meta property="og:title" content="{html.escape(p['title'],quote=True)} | Ultimate Deck Building Toolkit"><meta property="og:description" content="{html.escape(p['summary'],quote=True)}"><meta property="og:type" content="website"><meta property="og:image" content="https://www.unrealtools.com{BASE}assets/cover.jpg"><link rel="icon" href="/favicon.svg"><link rel="stylesheet" href="{BASE}assets/docs.css"><script defer src="{BASE}assets/docs.js"></script></head><body>
<a class="skip" href="#main">Skip to content</a><header class="top"><a class="brand" href="/"><svg width="24" height="24" viewBox="0 0 24 24" aria-hidden="true"><rect x="2" y="2" width="20" height="20" rx="5" fill="none" stroke="currentColor"/><path d="M7 8h10M7 12h10M7 16h6" stroke="currentColor"/></svg>Unreal Tools</a><a class="product" href="{BASE}">Deck Toolkit <span>/ Docs</span></a><button id="nav-toggle" aria-expanded="false" aria-controls="docs-nav">Browse docs</button><a class="home-link" href="/#tools">All tools ↗</a></header>
<div class="layout"><aside class="sidebar" id="docs-nav"><div class="sidebar-label">ULTIMATE DECK<br>BUILDING TOOLKIT</div><label for="doc-search">Find a topic</label><input id="doc-search" type="search" placeholder="Search documentation" autocomplete="off" aria-controls="search-results"><div id="search-results" aria-live="polite"></div><nav aria-label="Documentation">{nav}</nav><div class="sidebar-version">0.3.0 / UE 5.8 / WIN64</div></aside>
<main id="main"><div class="eyebrow">DECK TOOLKIT / DOCUMENTATION</div><h1>{p['title']}</h1><p class="summary">{p['summary']}</p><article>{p['body']}</article><nav class="pager" aria-label="Previous and next topic">{prev}{nxt}</nav><footer>© 2026 Hungry Ghost / Unreal Tools.<br>Independent tools for Unreal Engine. Not affiliated with or endorsed by Epic Games.<br><span>Documentation for version 0.3.0 · Updated September 10, 2026</span></footer></main><aside class="toc"><div class="sidebar-label">ON THIS PAGE</div><nav aria-label="On this page">{toc}</nav><a class="back-top" href="#main">Back to top ↑</a></aside></div></body></html>'''
    dest=OUT/p['slug'];dest.mkdir(exist_ok=True);(dest/'index.html').write_text(doc.encode('ascii', 'xmlcharrefreplace').decode('ascii'),encoding='ascii')
    search.append({'title':p['title'],'url':url(p),'summary':p['summary'],'text':html.unescape(re.sub('<[^>]+>',' ',p['body']))})
(OUT/'assets/search.json').write_text(json.dumps(search,ensure_ascii=True),encoding='utf-8')
print(f'Built {len(PAGES)} documentation pages.')
