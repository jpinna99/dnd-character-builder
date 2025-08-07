fetch('soveliss-stats.json')
    .then(response => {
    if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
    }
    return response.json();
    })

    .then(data => {
        const lookUpQuickStats = document.getElementById('look-up-quick-stats');
        lookUpQuickStats.addEventListener('click', (e) => {
            const infoContainer = document.getElementById('info-container');
            infoContainer.innerHTML = '';
            const newInfo = document.createElement('div');
            const SovName = document.createElement('p');
            SovName.innerHTML = "Name: " + JSON.stringify(data.name, null, 2);
            newInfo.appendChild(SovName);
            const SovLevel = document.createElement('p');
            SovLevel.innerText = "Level: " + JSON.stringify(data.level, null, 2);
            newInfo.appendChild(SovLevel);
            const SovAge = document.createElement('p');
            SovAge.innerText = "Age: " + JSON.stringify(data.age, null, 2);
            newInfo.appendChild(SovAge);
            const SovGender = document.createElement('p');
            SovGender.innerText = "Gender: " + JSON.stringify(data.gender, null, 2);
            newInfo.appendChild(SovGender);        
            const SovAlignment = document.createElement('p');
            SovAlignment.innerText = "Alignment: " + JSON.stringify(data.alignment, null, 2);
            newInfo.appendChild(SovAlignment);
            const SovSize = document.createElement('p');
            SovSize.innerText = "Size: " + JSON.stringify(data.size, null, 2);
            newInfo.appendChild(SovSize);
            const SovSpeed = document.createElement('p');
            SovSpeed.innerText = "Speed: " + JSON.stringify(data.speed, null, 2);
            newInfo.appendChild(SovSpeed);
            const SovLanguages = document.createElement('p');
            SovLanguages.innerText = "Languages: " + JSON.stringify(data.languages, null, 2);
            newInfo.appendChild(SovLanguages);
            const SovRaceSubRace = document.createElement('p');
            SovRaceSubRace.innerText = "Race: " + JSON.stringify(data.race, null, 2) + "  Subrace: " + JSON.stringify(data.subrace, null, 2);
            newInfo.appendChild(SovRaceSubRace);
            const SovClass = document.createElement('p');
            SovClass.innerHTML = "Class: " + JSON.stringify(data.DnDclass, null, 2);
            newInfo.appendChild(SovClass)
            const SovBackground = document.createElement('p');
            SovBackground.innerHTML = "Background: " + JSON.stringify(data.background, null, 2);
            newInfo.appendChild(SovBackground);
            const SovProficiencies = document.createElement('p');
            SovProficiencies.innerHTML = "Proficiencies: " + JSON.stringify(data.proficiencies, null, 2) + " Drow Proficiencies: " + JSON.stringify(data.drow_proficiencies, null, 2) + " Elf Proficiencies: " + JSON.stringify(data.elf_features['keen senses'], null, 2) + " Sage Proficiencies: " + JSON.stringify(data.sage_skill_proficiencies, null, 2);
            newInfo.appendChild(SovProficiencies);
            const SovDarkVision = document.createElement('p');
            SovDarkVision.innerHTML = "Darkvision: " + JSON.stringify(data.darkvision, null, 2) + " feet";
            newInfo.appendChild(SovDarkVision)
            infoContainer.appendChild(newInfo);
        })

        const lookUpHP = document.getElementById("look-up-HP");
        lookUpHP.addEventListener('click', (e) => {
            const infoContainer = document.getElementById('info-container');
            infoContainer.innerHTML = '';
            const newInfo = document.createElement('div');
            const SovHP = document.createElement('p');
            SovHP.innerHTML = "HP: " + JSON.stringify(data.HP, null, 2);
            newInfo.appendChild(SovHP);
            infoContainer.appendChild(newInfo);
        })

        const lookUpAC = document.getElementById("look-up-armor-class");
        lookUpAC.addEventListener('click', (e) => {
            const infoContainer = document.getElementById('info-container');
            infoContainer.innerHTML = '';
            const newInfo = document.createElement('div');
            const SovAC = document.createElement('p');
            SovAC.innerHTML = "Armor Class: " + JSON.stringify(data.armor_class, null, 2);
            newInfo.appendChild(SovAC);
            infoContainer.appendChild(newInfo);
        })

        const lookUpPB = document.getElementById("look-up-prof-bonus");
        lookUpPB.addEventListener('click', (e) => {
            const infoContainer = document.getElementById('info-container');
            infoContainer.innerHTML = '';
            const newInfo = document.createElement('div');
            const SovPB = document.createElement('p');
            SovPB.innerHTML = "Proficiency Bonus: " + JSON.stringify(data.proficiency_bonus, null, 2);
            newInfo.appendChild(SovPB);
            infoContainer.appendChild(newInfo);
        })

        const lookUpAbilityScores = document.getElementById('look-up-ability-scores');
        lookUpAbilityScores.addEventListener('click', e => {
            const infoContainer = document.getElementById('info-container');
            infoContainer.innerHTML = '';
            const newInfo = document.createElement('div');
            const SovStr = document.createElement('p');
            SovStr.innerHTML = "Strengh: " + JSON.stringify(data.ability_scores.strength, null, 2);
            newInfo.appendChild(SovStr);
            const SovDex = document.createElement('p');
            SovDex.innerHTML = "Dexterity: " + JSON.stringify(data.ability_scores.dexterity, null, 2);
            newInfo.appendChild(SovDex);
            const SovCon = document.createElement('p');
            SovCon.innerHTML = "Constitution: " + JSON.stringify(data.ability_scores.constitution, null, 2);
            newInfo.appendChild(SovCon);
            const SovInt = document.createElement('p');
            SovInt.innerHTML = "Intelligence: " + JSON.stringify(data.ability_scores.intelligence, null, 2);
            newInfo.appendChild(SovInt);
            const SovWis = document.createElement('p');
            SovWis.innerHTML = "Wisdom: " + JSON.stringify(data.ability_scores.wisdom, null, 2);
            newInfo.appendChild(SovWis);
            const SovCha = document.createElement('p');
            SovCha.innerHTML = "Charisma: " + JSON.stringify(data.ability_scores.charisma, null, 2);
            newInfo.appendChild(SovCha);
           
            infoContainer.appendChild(newInfo);
        })

        const lookUpSavingThrows = document.getElementById('look-up-saving-throws');
        lookUpSavingThrows.addEventListener('click', e => {
            const infoContainer = document.getElementById('info-container');
            infoContainer.innerHTML = '';
            const newInfo = document.createElement('div');
            const SovStr = document.createElement('p');
            SovStr.innerHTML = "Strengh: " + JSON.stringify(data.saving_throws.strength, null, 2);
            newInfo.appendChild(SovStr);
            const SovDex = document.createElement('p');
            SovDex.innerHTML = "Dexterity: " + JSON.stringify(data.saving_throws.dexterity, null, 2);
            newInfo.appendChild(SovDex);
            const SovCon = document.createElement('p');
            SovCon.innerHTML = "Constitution: " + JSON.stringify(data.saving_throws.constitution, null, 2);
            newInfo.appendChild(SovCon);
            const SovInt = document.createElement('p');
            SovInt.innerHTML = "Intelligence: " + JSON.stringify(data.saving_throws.intelligence, null, 2);
            newInfo.appendChild(SovInt);
            const SovWis = document.createElement('p');
            SovWis.innerHTML = "Wisdom: " + JSON.stringify(data.saving_throws.wisdom, null, 2);
            newInfo.appendChild(SovWis);
            const SovCha = document.createElement('p');
            SovCha.innerHTML = "Charisma: " + JSON.stringify(data.saving_throws.charisma, null, 2);
            newInfo.appendChild(SovCha);
            const SovAdvantages = document.createElement('p');
            SovAdvantages.innerHTML = JSON.stringify(data.elf_features['fey ancestry'][0], null, 2);
            newInfo.appendChild(SovAdvantages);
            infoContainer.appendChild(newInfo);
        })

        const lookUpSkills = document.getElementById('look-up-skills');
        lookUpSkills.addEventListener('click', e => {
            const infoContainer = document.getElementById('info-container');
            infoContainer.innerHTML = '';
            const newInfo = document.createElement('div');
            const SovSkills = document.createElement('p');
            SovSkills.innerHTML = JSON.stringify(data.skills, null, 2);
            newInfo.appendChild(SovSkills);
            infoContainer.appendChild(newInfo);
        })

        const lookUpImmunities = document.getElementById('look-up-immunities');
        lookUpImmunities.addEventListener('click', e => {
            const infoContainer = document.getElementById('info-container');
            infoContainer.innerHTML = '';
            const newInfo = document.createElement('div');
            const SovImmunities = document.createElement('p');
            SovImmunities.innerHTML = "Immunities: " + JSON.stringify(data.immunities, null, 2);
            newInfo.appendChild(SovImmunities);
            infoContainer.appendChild(newInfo);
        })

        const lookUpWealth = document.getElementById('look-up-wealth');
        lookUpWealth.addEventListener('click', e => {
            const infoContainer = document.getElementById('info-container');
            infoContainer.innerHTML = '';
            const newInfo = document.createElement('div');
            const SovWealth = document.createElement('p');
            SovWealth.innerHTML = JSON.stringify(data.wealth, null, 2);
            newInfo.appendChild(SovWealth);
            infoContainer.appendChild(newInfo);
        })

        const lookUpInspiration = document.getElementById("look-up-inspiration");
        lookUpInspiration.addEventListener('click', e => {
            const infoContainer = document.getElementById('info-container');
            infoContainer.innerHTML = '';
            const newInfo = document.createElement('div');
            const SovInspo = document.createElement('p');
            SovInspo.innerHTML = JSON.stringify(data.has_inspiration, null, 2);
            newInfo.appendChild(SovInspo);
            const SovInspoDie = document.createElement('p');
            SovInspoDie.innerHTML = JSON.stringify(data.inspiration_die, null, 2);
            newInfo.appendChild(SovInspoDie);
            infoContainer.appendChild(newInfo);
        })


        const lookUpCantrips = document.getElementById("look-up-cantrips");
        lookUpCantrips.addEventListener('click', e => {
            const infoContainer = document.getElementById('info-container');
            infoContainer.innerHTML = '';
            const newInfo = document.createElement('div');
            const parsedDataWarlock = JSON.parse(JSON.stringify(data.spells["warlock"]["cantrips"]["cantrip list"]));
            for (let cantrip of parsedDataWarlock) {
                let cantripdata = document.createElement('p');
                cantripdata.innerHTML = JSON.stringify(cantrip, null, 2);
                newInfo.appendChild(cantripdata);
                let spacer = document.createElement('p');
                spacer.style.marginBottom = '2px';
                spacer.innerHTML = "------";
                newInfo.appendChild(spacer);
            }
            const parsedDataSorcerer = JSON.parse(JSON.stringify(data.spells["sorcerer"]["cantrips"]["cantrip list"]));
            for (let cantrip of parsedDataSorcerer) {
                let cantripdata = document.createElement('p');
                cantripdata.innerHTML = JSON.stringify(cantrip, null, 2);
                newInfo.appendChild(cantripdata);
                let spacer = document.createElement('p');
                spacer.style.marginBottom = '2px';
                spacer.innerHTML = "------";
                newInfo.appendChild(spacer);
            }
            infoContainer.appendChild(newInfo);
        })

        const lookUpSpells = document.getElementById("look-up-spells");
        lookUpSpells.addEventListener('click', e => {
            const infoContainer = document.getElementById('info-container');
            infoContainer.innerHTML = '';
            const newInfo = document.createElement('div');
            const parsedDataWarlock = JSON.parse(JSON.stringify(data.spells["warlock"]["spells"]["spell list"]));
            for (let spell of parsedDataWarlock) {
                let spelldata = document.createElement('p');
                spelldata.innerHTML = JSON.stringify(spell, null, 2);
                newInfo.appendChild(spelldata);
                let spacer = document.createElement('p');
                spacer.style.marginBottom = '2px';
                spacer.innerHTML = "------";
                newInfo.appendChild(spacer);
            }
            const parsedDatSorcerer = JSON.parse(JSON.stringify(data.spells["sorcerer"]["spells"]["spell list"]));
            for (let spell of parsedDatSorcerer) {
                let spelldata = document.createElement('p');
                spelldata.innerHTML = JSON.stringify(spell, null, 2);
                newInfo.appendChild(spelldata);
                let spacer = document.createElement('p');
                spacer.style.marginBottom = '2px';
                spacer.innerHTML = "------";
                newInfo.appendChild(spacer);
            }
            infoContainer.appendChild(newInfo);
        })

        const lookUpConcentrationSpells = document.getElementById("look-up-concentraion-spells");
        lookUpConcentrationSpells.addEventListener('click', e => {
            const infoContainer = document.getElementById('info-container');
            infoContainer.innerHTML = '';
            const newInfo = document.createElement('div');
            const parsedCantripDataWarlock = JSON.parse(JSON.stringify(data.spells['warlock']["cantrips"]["cantrip list"]));
            for (let cantrip of parsedCantripDataWarlock) {
                if (cantrip.concentration === true || cantrip.concentration == 'yes') {
                    let cantripdata = document.createElement('p');
                    cantripdata.innerHTML = JSON.stringify(cantrip, null, 2);
                    newInfo.appendChild(cantripdata);
                    let spacer = document.createElement('p');
                    spacer.style.marginBottom = '2px';
                    spacer.innerHTML = "------";
                    newInfo.appendChild(spacer);
                }
            }
            const parsedSpellDataWarlock = JSON.parse(JSON.stringify(data.spells['warlock']["spells"]["spell list"]));
            for (let spell of parsedSpellDataWarlock) {
                if (spell.concentration === true || spell.concentration == 'yes') {
                    let spelldata = document.createElement('p');
                    spelldata.innerHTML = JSON.stringify(spell, null, 2);
                    newInfo.appendChild(spelldata);
                    let spacer = document.createElement('p');
                    spacer.style.marginBottom = '2px';
                    spacer.innerHTML = "------";
                    newInfo.appendChild(spacer);
                }
            }
            const parsedCantripDataSorcerer = JSON.parse(JSON.stringify(data.spells['sorcerer']["cantrips"]["cantrip list"]));
            for (let cantrip of parsedCantripDataSorcerer) {
                if (cantrip.concentration === true || cantrip.concentration == 'yes') {
                    let cantripdata = document.createElement('p');
                    cantripdata.innerHTML = JSON.stringify(cantrip, null, 2);
                    newInfo.appendChild(cantripdata);
                    let spacer = document.createElement('p');
                    spacer.style.marginBottom = '2px';
                    spacer.innerHTML = "------";
                    newInfo.appendChild(spacer);
                }
            }
            const parsedSpellDataSorcerer = JSON.parse(JSON.stringify(data.spells['sorcerer']["spells"]["spell list"]));
            for (let spell of parsedSpellDataSorcerer) {
                if (spell.concentration === true || spell.concentration == 'yes') {
                    let spelldata = document.createElement('p');
                    spelldata.innerHTML = JSON.stringify(spell, null, 2);
                    newInfo.appendChild(spelldata);
                    let spacer = document.createElement('p');
                    spacer.style.marginBottom = '2px';
                    spacer.innerHTML = "------";
                    newInfo.appendChild(spacer);
                }
            }
            infoContainer.appendChild(newInfo);
        })
                
        const lookUpSpellSlots = document.getElementById("look-up-spell-slots");
        lookUpSpellSlots.addEventListener('click', e => {
            const infoContainer = document.getElementById('info-container');
            infoContainer.innerHTML = '';
            const newInfo = document.createElement('div');
            const SovWarlockSpellSlots = document.createElement('p');
            SovWarlockSpellSlots.innerHTML = "Warlock: " + JSON.stringify(data.spells['warlock']['spell slots'], null, 2);
            const SovSorcererSpellSlots = document.createElement('p');
            SovSorcererSpellSlots.innerHTML = "Sorcerer: " + JSON.stringify(data.spells['sorcerer']['spells']['spell slots'], null, 2);
            newInfo.appendChild(SovWarlockSpellSlots);
            newInfo.appendChild(SovSorcererSpellSlots);
            infoContainer.appendChild(newInfo);
        })

        const lookUpSpellAttackMod = document.getElementById("look-up-spell-attack-mod");
        lookUpSpellAttackMod.addEventListener('click', e => {
            const infoContainer = document.getElementById('info-container');
            infoContainer.innerHTML = '';
            const newInfo = document.createElement('div');
            const SovSpellAttackMod = document.createElement('p');
            SovSpellAttackMod.innerHTML = "Spell Attack Modifer: " + JSON.stringify(data.spell_attack_modifier, null, 2);
            newInfo.appendChild(SovSpellAttackMod);
            infoContainer.appendChild(newInfo);
        })

        const lookUpSpellSaveDC = document.getElementById("look-up-spell-save-DC");
        lookUpSpellSaveDC.addEventListener('click', e => {
            const infoContainer = document.getElementById('info-container');
            infoContainer.innerHTML = '';
            const newInfo = document.createElement('div');
            const SovSpellSaveDC = document.createElement('p');
            SovSpellSaveDC.innerHTML = "Spell Save DC: " + JSON.stringify(data.spell_save_DC, null, 2);
            newInfo.appendChild(SovSpellSaveDC);
            infoContainer.appendChild(newInfo);
        })

        const lookUpInvocations = document.getElementById("look-up-invocations");
        lookUpInvocations.addEventListener('click', e => {
            const infoContainer = document.getElementById('info-container');
            infoContainer.innerHTML = '';
            const newInfo = document.createElement('div');
            const parsedData = JSON.parse(JSON.stringify(data.invocations["invocations list"]));
            for (let invocation of parsedData) {
                let invocationdata = document.createElement('p');
                invocationdata.innerHTML = JSON.stringify(invocation);
                newInfo.appendChild(invocationdata);
                let spacer = document.createElement('p');
                spacer.style.marginBottom = '2px';
                spacer.innerHTML = "------";
                newInfo.appendChild(spacer);
            }
            infoContainer.appendChild(newInfo);
        })

        const lookUpShadowArmor = document.getElementById("look-up-shadow-armor");
        lookUpShadowArmor.addEventListener('click', e => {
            const infoContainer = document.getElementById('info-container');
            infoContainer.innerHTML = '';
            const newInfo = document.createElement('div');
            const SovShadowArmor = document.createElement('div');
            const shadowArmorName = document.createElement('p');
            shadowArmorName.innerHTML = "Name: " + JSON.stringify(data.shadow_armor.name, null, 2);
            SovShadowArmor.appendChild(shadowArmorName);
            const shadowArmorLevel = document.createElement('p');
            shadowArmorLevel.innerHTML = "Level: " + JSON.stringify(data.shadow_armor.level, null, 2);
            SovShadowArmor.appendChild(shadowArmorLevel);
            const shadowArmorDesc = document.createElement('p');
            shadowArmorDesc.innerHTML = "Description: " + JSON.stringify(data.shadow_armor.description, null, 2);
            SovShadowArmor.appendChild(shadowArmorDesc);
            const shadowArmorActionType = document.createElement('p');
            shadowArmorActionType.innerHTML = "Action Type: " + JSON.stringify(data.shadow_armor['action type'], null, 2);
            SovShadowArmor.appendChild(shadowArmorActionType);
            const shadowArmorEffect = document.createElement('p');
            shadowArmorEffect.innerHTML = "Effect: " + JSON.stringify(data.shadow_armor.effect, null, 2);
            SovShadowArmor.appendChild(shadowArmorEffect);
            const shadowArmorNumOfUses = document.createElement('p');
            shadowArmorNumOfUses.innerHTML = "Number of Uses: " + JSON.stringify(data.shadow_armor["number of uses"], null, 2) + " (" + JSON.stringify(data.ability_scores['charisma']['modifier'], null, 2) + ")";
            SovShadowArmor.appendChild(shadowArmorNumOfUses);
            const shadowArmorNumOfUsesRemaining = document.createElement('p');
            shadowArmorNumOfUsesRemaining.innerHTML = "Number of Uses Remaining: " + JSON.stringify(data.shadow_armor["number of uses remaining"], null, 2);
            SovShadowArmor.appendChild(shadowArmorNumOfUsesRemaining);
            newInfo.appendChild(SovShadowArmor);
            infoContainer.appendChild(newInfo);
        })

        const lookUpReapersBlade = document.getElementById("look-up-reapers-blade");
        lookUpReapersBlade.addEventListener('click', e => {
            const infoContainer = document.getElementById('info-container');
            infoContainer.innerHTML = '';
            const newInfo = document.createElement('div');
            const SovReapersBlade = document.createElement('div');
            const reapersBladeName = document.createElement('p');
            reapersBladeName.innerHTML = "Name: " + JSON.stringify(data.reapers_blade.name, null, 2);
            SovReapersBlade.appendChild(reapersBladeName);
            const reapersBladeLevel = document.createElement('p');
            reapersBladeLevel.innerHTML = "Level: " + JSON.stringify(data.reapers_blade.level, null, 2);
            SovReapersBlade.appendChild(reapersBladeLevel);
            const reapersBladeDesc = document.createElement('p');
            reapersBladeDesc.innerHTML = "Description: " + JSON.stringify(data.reapers_blade.description, null, 2);
            SovReapersBlade.appendChild(reapersBladeDesc);
            const reapersBladeHigherLevels = document.createElement('p');
            reapersBladeHigherLevels.innerHTML = "Higher Levels: " + JSON.stringify(data.reapers_blade["higher levels"], null, 2);
            SovReapersBlade.appendChild(reapersBladeHigherLevels);
            const reapersBladeActionType = document.createElement('p');
            reapersBladeActionType.innerHTML = "Action Type: " + JSON.stringify(data.reapers_blade["action type"], null, 2);
            SovReapersBlade.appendChild(reapersBladeActionType);
            const reapersBladeNumOfUses = document.createElement('p');
            reapersBladeNumOfUses.innerHTML = "Number of Uses: " + JSON.stringify(data.reapers_blade["number of uses"], null, 2) + " (" + JSON.stringify(data.ability_scores['charisma']['modifier'], null, 2) + ")";
            SovReapersBlade.appendChild(reapersBladeNumOfUses);
            const reapersBladeNumOfUsesRemaining = document.createElement('p');
            reapersBladeNumOfUsesRemaining.innerHTML = "Number of Uses Remaining: " + JSON.stringify(data.reapers_blade["number of uses remaining"], null, 2);
            SovReapersBlade.appendChild(reapersBladeNumOfUsesRemaining);
            newInfo.appendChild(SovReapersBlade);
            infoContainer.appendChild(newInfo);
        })

        const lookUpWeapons = document.getElementById("look-up-weapons");
        lookUpWeapons.addEventListener('click', e => {
            const infoContainer = document.getElementById('info-container');
            infoContainer.innerHTML = '';
            const newInfo = document.createElement('div');
            const weaponsHeader = document.createElement('p');
            weaponsHeader.innerHTML = 'Weapons (all): ';
            newInfo.appendChild(weaponsHeader);
            for (let weapon in data.equipment.weapons) {
                let item = document.createElement('p');
                item.innerHTML = `${JSON.stringify(weapon, null, 2)}: ${JSON.stringify(data.equipment.weapons[weapon], null, 2)}`
                newInfo.appendChild(item);
            }
            const spacer = document.createElement('p');
            spacer.innerHTML = "---------------------"
            newInfo.appendChild(spacer);
            const SovWeaponsActive = document.createElement('p');
            SovWeaponsActive.innerHTML = "Weapons (active): " + JSON.stringify(data.equipment.active.weapons, null, 2);    
            newInfo.appendChild(SovWeaponsActive);
            infoContainer.appendChild(newInfo);
        })

        const lookUpGear = document.getElementById("look-up-gear");
        lookUpGear.addEventListener('click', e => {
            const infoContainer = document.getElementById('info-container');
            infoContainer.innerHTML = '';
            const newInfo = document.createElement('div');
            const SovGear = document.createElement('div');
            const equipmentList = data.equipment
            for (let key in equipmentList) {
                if (key !== 'weapons' && key !== 'active' && key !== 'armor') {
                    let newEntry = document.createElement('p');
                    newEntry.innerHTML = `${key}: ${JSON.stringify(data.equipment[key], null, 2)}`;
                    SovGear.appendChild(newEntry);
                }
            }
            newInfo.appendChild(SovGear);
            infoContainer.appendChild(newInfo);
        })

        const lookUpActions = document.getElementById("look-up-actions");
        lookUpActions.addEventListener('click', e => {
            const infoContainer = document.getElementById('info-container');
            infoContainer.innerHTML = '';
            const newInfo = document.createElement('div');
            const SovActions = document.createElement('div');
            const cantripListWarlock = data.spells.warlock.cantrips['cantrip list'];
            const cantripListSorcerer = data.spells.sorcerer.cantrips['cantrip list'];
            const spellListWarlock = data.spells.warlock.spells['spell list'];
            const spellListSorcerer = data.spells.sorcerer.spells['spell list'];
            const attackActions = document.createElement('p');
            attackActions.innerHTML = "Attack:  weapons " + JSON.stringify(data.equipment.active.weapons, null, 2); 
            SovActions.appendChild(attackActions);
            const cantripActionsWarlock = document.createElement('p');
            const cantripActionsSorcerer = document.createElement('p');
            cantripActionsWarlock.innerHTML = "Warlock cantrips: " + JSON.stringify(cantripListWarlock.map((cantrip) => cantrip.casting_time === '1 action' ? cantrip.name: ""));
            cantripActionsSorcerer.innerHTML = "Sorcerer cantrips: " + JSON.stringify(cantripListSorcerer.map((cantrip) => cantrip.casting_time === '1 action' ? cantrip.name: ""));
            SovActions.appendChild(cantripActionsWarlock);
            SovActions.appendChild(cantripActionsSorcerer);
            const spellActionsWarlock = document.createElement('p');
            const spellActionsSorcerer = document.createElement('p');
            spellActionsWarlock.innerHTML = "Warlock spells: " + JSON.stringify(spellListWarlock.map((spell) => spell.casting_time === '1 action' ? spell.name: ""));
            spellActionsSorcerer.innerHTML = "Sorcerer spells: " + JSON.stringify(spellListSorcerer.map((spell) => spell.casting_time === '1 action' ? spell.name: ""));
            SovActions.appendChild(spellActionsWarlock);
            SovActions.appendChild(spellActionsSorcerer);
            const reapersBlade = document.createElement('p');
            reapersBlade.innerHTML = "Reaper's Blade: summon blade to your side";
            SovActions.appendChild(reapersBlade);
            newInfo.appendChild(SovActions);
            infoContainer.appendChild(newInfo);
        })

        const lookUpBonusActions = document.getElementById("look-up-bonus-actions");
        lookUpBonusActions.addEventListener('click', e => {
            const infoContainer = document.getElementById('info-container');
            infoContainer.innerHTML = '';
            const newInfo = document.createElement('div');
            const SovBonusActions = document.createElement('div');
            const SovDancingLightsBonusAction = document.createElement('p');
            SovDancingLightsBonusAction.innerHTML = `Dancing Lights: As a bonus action on your turn, you can move the lights up to 60 feet to a new spot within range. A light must be within 20 feet of another light created by this spell, and a light winks out if it exceeds the spell's range (120 feet).`;
            SovBonusActions.appendChild(SovDancingLightsBonusAction);
            const SovReapersBlade = document.createElement('p');
            SovReapersBlade.innerHTML = `Reaper's Blade: You may use a bonus action to move the blade up to 20ft away, up to maximum of 50ft from you. As part of that same bonus action, you may have the Blade attack a target within 10ft of it. Make a melee spell attack against the target and on a hit, deal 1d8 Necrotic damage (increases at levels 6 and 14).`;
            SovBonusActions.appendChild(SovReapersBlade);
            const SovBonusActionCantripsWarlock = document.createElement('div');
            for (let spell of data.spells.warlock.cantrips['cantrip list']) {
                if (spell['casting_time'] === "1 bonus action") {
                    let newspell = document.createElement('p')
                    newspell.innerHTML = `Warlock cantrip: ${JSON.stringify(spell["name"])}: ${JSON.stringify(spell["desc"])}`;
                    SovBonusActionCantripsWarlock.appendChild(newspell);
                }
            }
            const SovBonusActionCantripsSorcerer = document.createElement('div');
            for (let spell of data.spells.sorcerer.cantrips['cantrip list']) {
                if (spell['casting_time'] === "1 bonus action") {
                    let newspell = document.createElement('p')
                    newspell.innerHTML = `Sorcerer cantrip: ${JSON.stringify(spell["name"])}: ${JSON.stringify(spell["desc"])}`;
                    SovBonusActionCantripsSorcerer.appendChild(newspell);
                }
            }
            const SovBonusActionSpellsWarlock = document.createElement('div');
            for (let spell of data.spells.warlock.spells['spell list']) {
                if (spell['casting_time'] === "1 bonus action") {
                    let newspell = document.createElement('p')
                    newspell.innerHTML = `Warlock spell: ${JSON.stringify(spell["name"])}: ${JSON.stringify(spell["desc"])}`;
                    SovBonusActionSpellsWarlock.appendChild(newspell);
                }
            }
            const SovBonusActionSpellsSorcerer = document.createElement('div');
            for (let spell of data.spells.sorcerer.spells['spell list']) {
                if (spell['casting_time'] === "1 bonus action") {
                    let newspell = document.createElement('p')
                    newspell.innerHTML = `Sorcerer spell: ${JSON.stringify(spell["name"])}: ${JSON.stringify(spell["desc"])}`;
                    SovBonusActionSpellsWarlock.appendChild(newspell);
                }
            }
            SovBonusActions.appendChild(SovBonusActionCantripsWarlock);
            SovBonusActions.appendChild(SovBonusActionCantripsSorcerer);
            SovBonusActions.appendChild(SovBonusActionSpellsWarlock);
            SovBonusActions.appendChild(SovBonusActionSpellsSorcerer);
            newInfo.appendChild(SovBonusActions);
            infoContainer.appendChild(newInfo);
        })

        const lookUpReactions = document.getElementById("look-up-reactions");
        lookUpReactions.addEventListener('click', e => {
            const infoContainer = document.getElementById('info-container');
            infoContainer.innerHTML = '';
            const newInfo = document.createElement('div');
            const SovReactions = document.createElement('div');
            const SovShadowArmor = document.createElement('p');
            SovShadowArmor.innerHTML = JSON.stringify(data.shadow_armor.name, null, 2);
            SovReactions.appendChild(SovShadowArmor)
            newInfo.appendChild(SovReactions);
            infoContainer.appendChild(newInfo);
        }
        )
    })
    

    
    .catch(error => {
    console.error('Error fetching or parsing JSON:', error);
    });
